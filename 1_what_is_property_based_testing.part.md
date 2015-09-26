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
<!-- @include code/part1/naive_pqueue.py -->
```

$$$NOTES

Some simple code we want to test.

Naive implementation is easy to understand.

O(N) because Timsort.

$$$

### How we usually write tests

```python
<!-- @include code/part1/tests/test_pqueue_example.py -->
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
<!-- @include code/part1/tests/test_pqueue_magic.py -->
```
<!-- {_class="fragment"} -->

<br/>

<p class="fragment">...but how does `assert_correct` know what's correct?</p>

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
<!-- @include code/part1/tests/test_pqueue_sufficiently_advanced.py -->
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
<!-- @include code/part1/tests/test_pqueue_properties.py -->
```

$$$NOTES

This is a real test case that actually runs.

Not complete, though. Doesn't test `add()`.
