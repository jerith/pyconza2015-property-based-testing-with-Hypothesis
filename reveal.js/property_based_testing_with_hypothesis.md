## Property-based Testing With Hypothesis

<br/>

#### _Let Your Army of Robots Write Your Tests_

<br/>

<br/>

Jeremy Thurgood

PyconZA 2015

$$$NOTES

I spend a lot of my time writing tests, and I'm not very good at it.
(Measured by bugs that reach production.)

$$$
$$$

## Part 1

<br/>
<br/>
<br/>
<br/>

### What is property-based testing?

$$$NOTES

Demonstrate by example.

$$$

### An example

```python
class NaivePriorityQueue(object):
    """
    A priority queue moves the smallest item to the front.
    Naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort(reverse=True)

    def get(self):
        """Remove and return the smallest item."""
        return self._items.pop()

```

$$$NOTES

Some simple code we want to test.

Naive implementation is easy to understand.

O(N) because Timsort.

$$$

### How we usually write tests

```python
from naive_pqueue import NaivePriorityQueue

def mkpq(items):
    """Create and fill a NaivePriorityQueue."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    return pq

def test_get_only():
    """If there's only one item, we get that."""
    pq = mkpq(["a"])
    assert pq.get() == "a"
    assert len(pq) == 0

def test_get_both():
    """If there are two items, we get both in order."""
    pq = mkpq(["a", "b"])
    assert pq.get() == "a"
    assert pq.get() == "b"
    assert len(pq) == 0

def test_put_only():
    """If the queue is empty, putting is trivial."""
    pq = NaivePriorityQueue()
    pq.put("a")
    assert pq._items == ["a"]

def test_put_small():
    """If we put a small item, it lands at the front."""
    pq = mkpq(["b", "c"])
    pq.put("a")
    # Note: The front of the queue is the end of the list.
    assert pq._items == ["c", "b", "a"]

def test_put_big():
    """If we put a big item, it lands at the back."""
    pq = mkpq(["a", "b"])
    pq.put("c")
    # Note: The front of the queue is the end of the list.
    assert pq._items == ["c", "b", "a"]

# And many more that I didn't write because I got bored and
# wandered off to work on something more interesting or play
# videogames or eat lunch.

```

$$$NOTES

This is "example-based testing".

A typical unit test suite has lots of little tests that each test one thing.

Ideally, each code path is tested exactly once.

$$$

### Issues with example-based tests

* Tedious to write. <!--{_class="fragment hc"}-->

* Lots of repetitition. <!--{_class="fragment hc"}-->

* Painful to maintain. <!--{_class="fragment hc"}-->

* Focus on low-level details. <!--{_class="fragment hc"}-->

... But infinitely better than no tests at all. <!--{_class="fragment"}-->

$$$NOTES

People are bad at tedious things.

Can't see the forest for the trees.

$$$

### How we want to write tests

<br/>

In a world made of unicorns and kittens and rainbows...

<br/>

```python
from magic import assert_correct
from naive_pqueue import NaivePriorityQueue

assert_correct(NaivePriorityQueue)

```
<!--{_class="fragment"}-->

<br/>

...but how does `assert_correct` know what's correct?

<!--{_class="fragment"}-->

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
from sufficiently_advanced_technology import CorrectnessDefinition, number_list
from naive_pqueue import NaivePriorityQueue

class PriorityQueueCorrectnessDefinition(CorrectnessDefinition):

    def get_items_in_priority_order(self, items=number_list):
        """Priority: we always get the smallest item first."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        current = pq.get()
        while len(pq) > 0:
            prior, current = current, pq.get()
            assert prior <= current

    def get_all_items(self, items=number_list):
        """Queue: we always get every item exactly once."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        while len(pq) > 0:
            items.remove(pq.get())
        assert len(items) == 0

PriorityQueueCorrectnessDefinition.assert_correct()

```

$$$NOTES

We have some methods that test correctness *in general*.

We're only specifying the kind of input, not specific values.

$$$

### How property-based tests work

* Properties are assertions about invariants. <!--{_class="fragment hc"}-->

* Lots of checks with randomly generated input. <!--{_class="fragment hc"}-->

* Failure case minimization. <!--{_class="fragment hc"}-->

* Focus on high-level behaviour. <!--{_class="fragment hc"}-->

... But no silver bullet. <!--{_class="fragment"}-->

$$$NOTES

You like non-deterministic tests, right?

More on minimization later.

Lots of checks means lots of time.

$$$

### For real, with Hypothesis

```python
from hypothesis import given, strategies as st
from naive_pqueue import NaivePriorityQueue

@given(items=st.lists(st.integers()))
def test_get_all_items(items):
    """We get every item exactly once."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    while len(pq) > 0:
        items.remove(pq.get())
    assert len(items) == 0

@given(items=st.lists(st.integers(), min_size=1))
def test_get_items_in_order(items):
    """We get items in sorted order."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    current = pq.get()
    while len(pq) > 0:
        prior, current = current, pq.get()
        assert prior <= current

```

$$$NOTES

This is a real test case that actually runs.


$$$
$$$

## Part 2

<br/>
<br/>
<br/>
<br/>

### Hypothesis basics

$$$

### Anatomy of a test

<p>`@given` turns a test into a property ...</p>
<!--{_class="fragment hc"}-->

... that runs a bunch of times with random input ...
<!--{_class="fragment hc"}-->

... generated by the strategies you give it ...
<!--{_class="fragment hc"}-->

... and reports minimised failure examples.
<!--{_class="fragment hc"}-->

$$$NOTES

$$$

### Simple test

```python
from hypothesis import given, strategies as st

@given(st.floats())
def test_additive_inverse(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
failtest_additive_inverse_nan.py F
=============================== FAILURES ===============================
________________________ test_additive_inverse _________________________
[Traceback elided]
AssertionError: assert nan == --nan
------------------------------ Hypothesis ------------------------------
Falsifying example: test_additive_inverse(x=nan)
======================= 1 failed in 0.02 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Fails because `NaN` is not equal to anything.

$$$

### Assume valid input

We can `assume` our input isn't NaN.

```python
import math
from hypothesis import given, assume, strategies as st

@given(st.floats())
def test_additive_inverse(x):
    """Double additive inverse has no effect (except NaN)."""
    assume(not math.isnan(x))
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
test_additive_inverse_assume.py .
======================= 1 passed in 0.06 seconds =======================

```

$$$NOTES

Could also change the strategy.

$$$

### Settings

Let's see what Hypothesis is actually doing.

```python
from hypothesis import given, Settings, Verbosity, strategies as st

with Settings(max_examples=5, verbosity=Verbosity.verbose):
    @given(st.integers(-10, 10))
    def test_additive_inverse(x):
        """Double additive inverse has no effect."""
        assert x == -(-x)

if __name__ == "__main__":
    test_additive_inverse()

```

```pytestresult
Trying example: test_additive_inverse(x=9)
Trying example: test_additive_inverse(x=-8)
Trying example: test_additive_inverse(x=4)
Trying example: test_additive_inverse(x=3)
Trying example: test_additive_inverse(x=-3)

```

$$$NOTES

$$$

### Minimization

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sum_less_than_42(numbers):
    assert sum(numbers) < 42

```

```pytestresult
========================= test session starts ==========================
failtest_minimization.py F
=============================== FAILURES ===============================
________________________ test_sum_less_than_42 _________________________
[Traceback elided]
AssertionError: assert 42 < 42
 +  where 42 = sum([42])
------------------------------ Hypothesis ------------------------------
Falsifying example: test_sum_less_than_42(numbers=[42])
======================= 1 failed in 0.03 seconds =======================

```
<!--{_class="fragment" data-fragment-index="1"}-->

The example is (usually) the simplest failing input.
<!--{_class="fragment" data-fragment-index="1"}-->

$$$NOTES

What witchcraft is this!?

Minimization filters out the noise of random input.

$$$

### More minimization

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sum_less_than_42_nontrivial(numbers):
    if len(numbers) > 2:
        assert sum(numbers) < 42

```

```pytestresult
========================= test session starts ==========================
failtest_minimization_nontrivial.py F
=============================== FAILURES ===============================
___________________ test_sum_less_than_42_nontrivial ___________________
[Traceback elided]
AssertionError: assert 42 < 42
 +  where 42 = sum([0, 0, 42])
------------------------------ Hypothesis ------------------------------
Falsifying example: test_sum_less_than_42_nontrivial(numbers=[0, 0, 42])
======================= 1 failed in 0.05 seconds =======================

```

Works for more complicated cases as well.

$$$NOTES

Finds local minima.

Not perfect. Sometimes non-minimal data gets through.


$$$
$$$

## Part 3

<br/>
<br/>
<br/>
<br/>

### Generating values

$$$

### Strategies

A strategy is a set of rules:

* It knows how to generate values. <!--{_class="fragment hc" data-fragment-index="1"}-->
  *(Of course.)* <!--{_class="fragment vhc" data-fragment-index="1"}-->

* It knows how to simplify values. <!--{_class="fragment hc" data-fragment-index="2"}-->
  *(Very important!)* <!--{_class="fragment vhc" data-fragment-index="2"}-->

* It's composable. <!--{_class="fragment hc" data-fragment-index="3"}-->
  *(Building blocks for complex data.)* <!--{_class="fragment vhc" data-fragment-index="3"}-->

Built-in strategies are very clever so yours can be simple.
<!--{_class="fragment"}-->

$$$NOTES

Other tools call them generators.

Django models, too.

$$$

### Simple strategies

```python
>>> st.just("I'm so lonely.").example()
"I'm so lonely."

```

```python
>>> pprint((st.text("abc", max_size=5) | st.none()).example())
u'ccabc'
>>> pprint((st.text("abc", max_size=5) | st.none()).example())
None
>>> pprint((st.text("abc", max_size=5) | st.none()).example())
u''

```
<!--{_class="fragment"}-->

```python
>>> st.tuples(st.integers(0, 10), st.booleans()).example()
(2, True)
>>> st.tuples(st.integers(0, 10), st.booleans()).example()
(7, False)

```
<!--{_class="fragment"}-->

```python
>>> st.integers(0, 10).map(lambda x: 2 ** x).example()
1
>>> st.integers(0, 10).map(lambda x: 2 ** x).example()
512
>>> st.integers(0, 10).map(lambda x: 2 ** x).example()
8

```
<!--{_class="fragment"}-->

$$$NOTES

Beware duplicates when combining strategies.

$$$

### flatmap: square text

```python
from hypothesis.strategies import integers, text, lists

def text_line(size):
    return text("1234567890", min_size=size, max_size=size)

def square_lines(size):
    return lists(text_line(size), min_size=size, max_size=size)

square_text = integers(1, 5).flatmap(square_lines).map("\n".join)

```

```python
>>> print square_text.example()
42
44
>>> print square_text.example()
7
>>> print square_text.example()
5005
8274
9505
0599

```

$$$NOTES

You probably won't use this much.

$$$

### recursive: nested dicts

```python
from hypothesis.strategies import text, none, dictionaries, recursive

def nest_dict(values):
    return dictionaries(text("abc", max_size=5), values)

nested_dicts = recursive(text("def", max_size=5) | none(), nest_dict)

```

```python
>>> pprint(nested_dicts.example())
{}
>>> pprint(nested_dicts.example())
{u'': None,
 u'c': {},
 u'cc': None,
 u'ccccc': {u'b': {},
            u'bbb': {u'': None, u'a': None},
            u'cb': {u'': None, u'a': None, u'b': None}}}
>>> pprint(nested_dicts.example())
{u'': {u'': None, u'a': None}, u'bbabb': {}}
>>> pprint(nested_dicts.example())
u'fd'

```

$$$NOTES

This stuff is in the docs.


$$$
$$$

## Part 4

<br/>
<br/>
<br/>
<br/>

### Writing property-based tests

$$$

### What makes a good property?

* True for (almost) all input. <!--{_class="fragment hc"}-->

* Does not duplicate the code under test. <!--{_class="fragment hc"}-->

* Describes the code under test in a meaningful way. <!--{_class="fragment hc"}-->

* Not too expensive to check. <!--{_class="fragment hc"}-->

Harder than example-based tests, but a lot more useful. <!--{_class="fragment"}-->

$$$NOTES

Well-defined exceptions are okay, but test separately.

You'll be running these hundreds of times.

$$$

### Tips for defining properties

* <span>Idempotence</span> <!--{_class="fragment hc" data-fragment-index="1"}-->
  <span>*f( f(x) ) = f(x)*</span> <!--{_class="fragment vhc" data-fragment-index="1"}-->

* <span>Round trip</span> <!--{_class="fragment hc" data-fragment-index="2"}-->
  <span>*f<sup> -1</sup>( f(x) ) = x*</span> <!--{_class="fragment vhc" data-fragment-index="2"}-->

* <span>Invariance</span> <!--{_class="fragment hc" data-fragment-index="3"}-->
  <span>*g( f(x) ) = g(x)*</span> <!--{_class="fragment vhc" data-fragment-index="3"}-->

* <span>Transformation</span> <!--{_class="fragment hc" data-fragment-index="4"}-->
  <span>*f( g(x) ) = g'( f(x) )*</span> <!--{_class="fragment vhc" data-fragment-index="4"}-->

* <span>Verification</span> <!--{_class="fragment hc" data-fragment-index="5"}-->
  <span>*P( f(x) ) is true*</span> <!--{_class="fragment vhc" data-fragment-index="5"}-->

* <span>Oracle</span> <!--{_class="fragment hc" data-fragment-index="6"}-->
  <span>*f(x) = g(x)*</span> <!--{_class="fragment vhc" data-fragment-index="6"}-->

<!--{_class="sb"}-->

$$$NOTES

Verification example: Sorted list.

An oracle assumes a known-correct implementation to test against.

$$$

### Idempotence

```python
from hypothesis import given, strategies as st

@given(number=st.floats(-1e300, 1e300), decimals=st.integers(0, 5))
def test_round_idempotent(number, decimals):
    """
    Rounding an already-rounded number is a no-op.
    """
    rounded = round(number, decimals)
    assert rounded == round(rounded, decimals)

```

It's already been done.

$$$NOTES

$$$

### Round trip

```python
from hypothesis import given, strategies as st
import myjson

def nest_data(st_values):
    return st.lists(st_values) | st.dictionaries(st.text(), st_values)

def nested_data():
    return st.none() | st.integers() | st.floats(-1e308, 1e308) | st.text()


@given(st.recursive(nested_data(), nest_data))
def test_json_round_trip(data):
    """
    Encoding a thing as JSON and decoding it again returns the same thing.

    (This will fail for input that contains tuples, but we don't test that.)
    """
    assert data == myjson.loads(myjson.dumps(data))

```

There and back again.

$$$NOTES

Beware serialization differences.

$$$

### Invariance

```python
from hypothesis import given, strategies as st

@given(st.randoms(), st.lists(st.integers()))
def test_something_invariant(rand, items):
    """
    The set of items in a collection does not change when shuffling.
    """
    orig_items = list(items)
    rand.shuffle(items)
    for item in items:
        orig_items.remove(item)
    assert orig_items == []

```

Some things never change.

$$$NOTES

$$$

### Transformation

```python
from string import ascii_uppercase as uc, ascii_lowercase as lc, digits
from hypothesis import given, strategies as st

st_upperlower = st.sampled_from(zip(uc + digits, lc + digits))

@given(st_upperlower, st.text())
def test_uppercase_transformation(upperlower, text):
    """
    Appending a lowercase character before uppercasing is equivalent to
    appending its uppercase equivalent after uppercasing.
    """
    (upper, lower) = upperlower
    assert text.upper() + upper == (text + lower).upper()

```

All roads lead to Rome.

$$$NOTES

$$$

### Verification

```python
from hypothesis import given, strategies as st

@given(st.text("abcd \t\r\n"))
def test_no_tabs_after_expandtabs(text):
    """
    Expanding tabs replaces all tab characters.
    """
    assert "\t" not in text.expandtabs()

```

(e) None of the above.

$$$NOTES

This is true after the operation is performed.

$$$

### Oracle

```python
import json
from hypothesis import given, strategies as st
import myjson

def nest_data(st_values):
    return st.lists(st_values) | st.dictionaries(st.text(), st_values)

def nested_data():
    return st.none() | st.integers() | st.floats(-1e308, 1e308) | st.text()

@given(st.recursive(nested_data(), nest_data).map(json.dumps))
def test_json_oracle(json_text):
    """
    The new thing behaves the same as the old thing.
    """
    assert json.loads(json_text) == myjson.loads(json_text)

```

No, not the database.

$$$NOTES

Useful with a simple model or naive implementation.

$$$

### Back to our priority queue

```python
class NaivePriorityQueue(object):
    """
    A priority queue moves the smallest item to the front.
    Naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort(reverse=True)

    def get(self):
        """Remove and return the smallest item."""
        return self._items.pop()

```

$$$NOTES

Remember this guy? We don't want to use him in production.

$$$

### Much better priority queue

```python
class FastPriorityQueue(object):
    """
    A priority queue moves the smallest item to the front.
    Heap-based implementation with O(log N) `put()` and `get()`.
    """
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def put(self, item):
        """
        Add an item to the collection.
        """
        self._heap.append(item)
        self._swim(len(self))

    def get(self):
        """
        Remove and return the smallest item in the collection.
        """
        self._swap(1, len(self))
        item = self._heap.pop()
        self._sink(1)
        return item

    def _less(self, i, j):
        """
        True if i_val and j_val exist and i_val < j_val, else False.
        """
        if max([i, j]) > len(self):
            return False
        return self._heap[i-1] < self._heap[j-1]

    def _swap(self, i, j):
        """
        Swap i_val and j_val.
        """
        self._heap[i-1], self._heap[j-1] = self._heap[j-1], self._heap[i-1]

    def _swim(self, i):
        """
        Move i_val up the heap until it's in a valid position.

        While i_val is smaller than its parent, swap with the parent.
        """
        while i > 1 and self._less(i, i/2):
            self._swap(i, i/2)
            i /= 2

    def _sink(self, i):
        """
        Move i_val down the heap until it's in a valid position.

        While i_val is larger than any children, swap with the largest child.
        """
        while i < len(self):
            j = i*2
            if self._less(j+1, j):
                j += 1
            if not self._less(j, i):
                return
            self._swap(i, j)
            i = j

```

$$$NOTES

This guy is much better, but much more complex.

$$$

### Stateful tests

```python
from hypothesis import assume, strategies as st
from hypothesis.stateful import RuleBasedStateMachine, rule
from fast_pqueue import FastPriorityQueue

class PriorityQueueStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super(PriorityQueueStateMachine, self).__init__()
        self.items = []
        self.pq = FastPriorityQueue()

    @rule(item=st.integers())
    def check_put(self, item):
        assert len(self.pq) == len(self.items)
        self.pq.put(item)
        self.items.append(item)

    @rule()
    def check_get(self):
        assert len(self.pq) == len(self.items)
        assume(len(self.items) > 0)
        item = min(self.items)
        self.items.remove(item)
        assert self.pq.get() == item

TestPriorityQueue = PriorityQueueStateMachine.TestCase

```
<!--{_style="font-size:50%"}-->

$$$NOTES

We define the state machine, Hypothesis exercises it.

Show example.


$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
