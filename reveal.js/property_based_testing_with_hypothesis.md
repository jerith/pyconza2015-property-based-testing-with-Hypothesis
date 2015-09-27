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
    A priority queue is a collection which returns items in sorted order.
    This is a naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self, items=()):
        self._items = list(items)
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort()

    def get(self):
        """Remove and return the smallest item in the collection."""
        return self._items.pop(0)

```

$$$NOTES

Some simple code we want to test.

Naive implementation is easy to understand.

O(N) because Timsort.

$$$

### How we usually write tests

```python
from naive_pqueue import NaivePriorityQueue

def test_get_only():
    """If there's only one item, we get that."""
    pq = NaivePriorityQueue(["a"])
    assert pq.get() == "a"
    assert len(pq) == 0

def test_get_both():
    """If there are two items, we get both in order."""
    pq = NaivePriorityQueue(["a", "b"])
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
    pq = NaivePriorityQueue(["b", "c"])
    pq.put("a")
    assert pq._items == ["a", "b", "c"]

def test_put_big():
    """If we put a big item, it lands at the back."""
    pq = NaivePriorityQueue(["a", "b"])
    pq.put("c")
    assert pq._items == ["a", "b", "c"]

```

$$$NOTES

This is "example-based testing".

A typical unit test suite has lots of little tests that each test one thing.

Ideally, each code path is tested exactly once.

$$$

### Issues with example-based tests

* Tedious to write. <!--{_class="fragment"}-->

* Lots of repetitition. <!--{_class="fragment"}-->

* Painful to maintain. <!--{_class="fragment"}-->

* Focus on low-level details. <!--{_class="fragment"}-->

* ... But infinitely better than no tests at all. <!--{_class="fragment"}-->

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
<!-- {_class="fragment"} -->

<br/>

<p class="fragment">...but how does `assert_correct` know what's correct?</p>

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
from sufficiently_advanced_technology import VerifyCorrect, number_list
from naive_pqueue import NaivePriorityQueue

class VerifyPriorityQueueCorrect(VerifyCorrect):
    def get_all_items(self, items=number_list):
        """We get every item exactly once."""
        pq = NaivePriorityQueue(items)
        while len(pq) > 0:
            items.remove(pq.get())
        assert len(items) == 0

    def get_items_in_order(self, items=number_list):
        """We get items in sorted order."""
        pq = NaivePriorityQueue(items)
        prior = current = pq.get()
        while len(pq) > 0:
            prior, current = current, pq.get()
            assert prior <= current

VerifyPriorityQueueCorrect.assert_correct()

```

$$$NOTES

We have some methods that test correctness *in general*.

Not complete, though. Doesn't test `add()`.

We're only specifying the kind of input, not specific values.

$$$

### How property-based tests work

* Properties are assertions about invariants. <!--{_class="fragment"}-->

* Lots of checks with randomly generated input. <!--{_class="fragment"}-->

* Failure case minimisation. <!--{_class="fragment"}-->

* Focus on high-level behaviour. <!--{_class="fragment"}-->

* ... But no silver bullet. <!--{_class="fragment"}-->

$$$NOTES

You like non-deterministic tests, right?

More on minimisation later.

Lots of checks means lots of time.

$$$

### For real, with Hypothesis

```python
from hypothesis import given, strategies as st
from naive_pqueue import NaivePriorityQueue

@given(items=st.lists(st.integers()))
def test_get_all_items(items):
    """We get every item exactly once."""
    pq = NaivePriorityQueue(items)
    while len(pq) > 0:
        items.remove(pq.get())
    assert len(items) == 0

@given(items=st.lists(st.integers(), min_size=1))
def test_get_items_in_order(items):
    """We get items in sorted order."""
    pq = NaivePriorityQueue(items)
    prior = current = pq.get()
    while len(pq) > 0:
        prior, current = current, pq.get()
        assert prior <= current

```

$$$NOTES

This is a real test case that actually runs.

Not complete, though. Doesn't test `add()`.


$$$
$$$

## Part 2

<br/>
<br/>
<br/>
<br/>

### Hypothesis basics

$$$

### Managing generated input <span style="opacity: 0.3">(1)</span>

Additive inverse (integers)

```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_additive_inverse_int(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
test_additive_inverse_int.py .
======================= 1 passed in 0.13 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Very simple example, valid for all integers.

$$$

### Managing generated input <span style="opacity: 0.3">(2)</span>

Additive inverse (floating point)

```python
from hypothesis import given, strategies as st

@given(st.floats())
def test_additive_inverse_float(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
failtest_additive_inverse_float.py F
=============================== FAILURES ===============================
_____________________ test_additive_inverse_float ______________________
[Traceback elided]
AssertionError: assert nan == --nan
------------------------------ Hypothesis ------------------------------
Falsifying example: test_additive_inverse_float(x=nan)
======================= 1 failed in 0.03 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Fails because `NaN` is not equal to anything.

$$$

### Managing generated input <span style="opacity: 0.3">(3)</span>

Additive inverse (floating point) without NaN

```python
import math
from hypothesis import given, assume, strategies as st

@given(st.floats())
def test_additive_inverse_float(x):
    """Double additive inverse has no effect (except NaN)."""
    assume(not math.isnan(x))
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
test_additive_inverse_float.py .
======================= 1 passed in 0.07 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

`assume()` tells Hypothesis to ignore this example.

$$$

### Managing generated input <span style="opacity: 0.3">(4)</span>

```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_weird_edge_case(x):
    """A number divided by itself is always 1."""
    assert (x - 1337) / (x - 1337) == 1

```

Note the potential division by zero.

```pytestresult
========================= test session starts ==========================
test_weird_edge_case.py .
======================= 1 passed in 0.06 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Random generation doesn't find everything.

Built-in strategies are cleverly weighted to include common edge cases.

$$$

### Managing generated input <span style="opacity: 0.3">(5)</span>

```python
from hypothesis import given, example, strategies as st

@example(1337)
@given(st.integers())
def test_weird_edge_case(x):
    """A number divided by itself is always 1, right?"""
    assert (x - 1337) / (x - 1337) == 1

```

We explicitly include the divide-by-zero input.

```pytestresult
========================= test session starts ==========================
failtest_weird_edge_case.py F
=============================== FAILURES ===============================
_________________________ test_weird_edge_case _________________________
[Traceback elided]
ZeroDivisionError: integer division or modulo by zero
------------------------------ Hypothesis ------------------------------
Falsifying example: test_weird_edge_case(x=1337)
======================= 1 failed in 0.01 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Random generation doesn't find everything.

Built-in strategies are cleverly weighted to include common edge cases.

$$$

### Strategies

A strategy is a set of rules:

* It knows how to generate values. <!--{_class="fragment"}-->
  *(Of course.)* <!--{_class="fragment"}-->

* It knows how to simplify values. <!--{_class="fragment"}-->
  *(Very important!)* <!--{_class="fragment"}-->

* It is composable. <!--{_class="fragment"}-->
  *(Building blocks for complex data.)* <!--{_class="fragment"}-->

Built-in strategies are very clever, so yours can be simple.
<!--{_class="fragment"}-->

$$$NOTES

Other tools call them generators.

.example() generates a random example.

$$$

### Strategies: combinations

ints or floats or strings:

```python
>>> ints_or_floats_or_strings = integers() | floats() | text("1234567890")
>>> ints_or_floats_or_strings.example()
u'25439943'
>>> ints_or_floats_or_strings.example()
-654234146027241025880061147001483025751L
>>> ints_or_floats_or_strings.example()
-0.7821238706527601
>>> ints_or_floats_or_strings.example()
-3.032482863887629e+132
>>> ints_or_floats_or_strings.example()
u'8666366964400506'

```

Beware:
<!--{_class="fragment" data-fragment-index="1"}-->

<span class="fragment" data-fragment-index="1">
`text()|none()` generates half strings, half `None`.
</span>

$$$NOTES

Sometimes you want to choose from multiple strategies.

$$$

### Strategies: filter and map

Lists with even lengths:

```python
>>> even_lists = lists(integers(0, 100)).filter(lambda l: len(l) % 2 == 0)
>>> even_lists.example()
[52, 42]
>>> even_lists.example()
[71, 34, 79, 50, 80, 56, 64, 34]
>>> even_lists.example()
[]

```

Odd integers:
<!--{_class="fragment" data-fragment-index="1"}-->

```python
>>> odd_integers = integers().map(lambda x: x * 2 + 1)
>>> odd_integers.example()
45
>>> odd_integers.example()
690832349825714274807131201360674962691L
>>> odd_integers.example()
-841

```
<!--{_class="fragment" data-fragment-index="1"}-->

$$$NOTES

Filter predicates mustn't be too hard to satisfy.

Use map instead of filter where possible.

$$$

### Strategies: flatmap

Square text:

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

### Strategies: recursive

Nested dicts:

```python
>>> nest_dict = lambda vs: dictionaries(text("abc", max_size=5), vs)
>>> nested_dicts = recursive(integers(0, 100) | none(), nest_dict)
>>> pprint(nested_dicts.example())
None
>>> pprint(nested_dicts.example())
{u'a': None, u'b': 49}
>>> pprint(nested_dicts.example())
28
>>> pprint(nested_dicts.example())
{}
>>> pprint(nested_dicts.example())
{u'': None,
 u'a': {},
 u'aa': {u'': 84,
         u'b': 13,
         u'bbb': 1,
         u'cbbcc': 84},
 u'b': 0}
>>> pprint(nested_dicts.example())
{u'': 54, u'c': 28, u'cc': 87, u'ccc': 35}

```

$$$NOTES

This stuff is in the docs.

$$$

### Minimization <span style="opacity: 0.3">(1)</span>

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
======================= 1 failed in 0.05 seconds =======================

```
<!--{_class="fragment"}-->

The falsifying example is the simplest failing input.
<!--{_class="fragment"}-->

$$$NOTES

What witchcraft is this!?

Minimization filters out the noise of random input.

$$$

### Minimization <span style="opacity: 0.3">(2)</span>

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
 +  where 42 = sum([0, 42, 0])
------------------------------ Hypothesis ------------------------------
Falsifying example: test_sum_less_than_42_nontrivial(numbers=[0, 42, 0])
======================= 1 failed in 0.11 seconds =======================

```

Works for more complicated cases as well.

$$$NOTES

Not perfect. Sometimes non-minimal data gets through.


$$$
$$$

## Part 3

<br/>
<br/>
<br/>
<br/>

### Stateful testing

$$$

### Back to our priority queue

```python
class NaivePriorityQueue(object):
    """
    A priority queue is a collection which returns items in sorted order.
    This is a naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self, items=()):
        self._items = list(items)
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort()

    def get(self):
        """Remove and return the smallest item in the collection."""
        return self._items.pop(0)

```

$$$NOTES

Very simple example, valid for all integers.


$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
