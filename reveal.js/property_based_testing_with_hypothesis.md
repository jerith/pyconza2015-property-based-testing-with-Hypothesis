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

Although these reimplement too much of the code under test.

We're only specifying the kind of input, not specific values.

But how does this Sufficiently Advanced Technology work?

$$$

### How property-based tests work

* Properties are assertions about invariants. <!--{_class="fragment"}-->

* Lots of checks with randomly generated input. <!--{_class="fragment"}-->

* Failure case minimisation. <!--{_class="fragment"}-->

* Focus on high-level behaviour. <!--{_class="fragment"}-->

* ... But no silver bullet. <!--{_class="fragment"}-->

$$$NOTES

You like non-deterministic tests, right?

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

### Hypothesis

$$$NOTES

$$$

### Writing tests

```python
from hypothesis import given, strategies as st


@given(st.integers())
def test_addition_identity(x):
    assert x + 0 == x


@given(st.integers(), st.integers())
def test_addition_commutative(x, y):
    assert x + y == y + x


@given(st.integers(), st.integers(), st.integers())
def test_addition_associative(x, y, z):
    assert (x + y) + z == x + (y + z)

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$

### Built-in Strategies

```python
>>> from hypothesis import strategies

>>> text = strategies.text()
>>> text.example()
u''
>>> text.example()
u'm<\x7f&\x02\u0393\r`\x8d<&\x1c\u0393mm\r\x1c\x18\x0c\x02\xa5'

>>> abctext = strategies.text(alphabet="abc")
>>> abctext.example()
u'cacaccccacaaacc'
>>> abctext.example()
u'aaaaaaaabaacabaaacaaaaaabaaaaac'

>>> lists_of_ints = strategies.lists(strategies.integers(-1000, 1000))
>>> lists_of_ints.example()
[-947, 873, -947, -37, 936, 936, 936]
>>> lists_of_ints.example()
[-805, 855, 674, -236, 447, 775, -168, -909, -512, 220, 994, 278, -803, -901]
>>> lists_of_ints.example()
[-75, 487, -468]

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$

### Adapting strategies: filter

```python
>>> even_lists = lists(integers(0, 100)).filter(lambda l: len(l) % 2 == 0)
>>> even_lists.example()
[52, 42]
>>> even_lists.example()
[71, 34, 79, 50, 80, 56, 64, 34]
>>> even_lists.example()
[]

```

$$$NOTES

$$$

### Adapting strategies: map

```python
>>> even_integers = strategies.integers().filter(lambda x: x % 2 == 0)
>>> even_integers.example()
-54
>>> even_integers.example()
0
>>> even_integers.example()
-110212872381391885439645758881510120016L


```

```python
>>> even_integers = strategies.integers().map(lambda x: x * 2)
>>> even_integers.example()
6
>>> even_integers.example()
-52
>>> even_integers.example()
-621603898346041721844744845583782563802L

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$


$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
