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
<!-- @include code/part1/test_pqueue_example.py -->
```

$$$NOTES

This is "example-based testing".

A typical unit test suite has lots of little tests that each test one thing.

Ideally, each code path is tested exactly once.

$$$

### Issues with example-based tests

* Tedious to write. <!--@exec frag("hc")-->

* Lots of repetitition. <!--@exec frag("hc")-->

* Painful to maintain. <!--@exec frag("hc")-->

* Focus on low-level details. <!--@exec frag("hc")-->

... But infinitely better than no tests at all. <!--@exec frag()-->

$$$NOTES

People are bad at tedious things.

Can't see the forest for the trees.

$$$

### How we want to write tests

<br/>

In a world made of unicorns and kittens and rainbows...

<br/>

```python
<!-- @include code/part1/test_pqueue_magic.py -->
```
<!--@exec frag()-->

<br/>

...but how does `assert_correct` know what's correct?

<!--@exec frag()-->

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
<!-- @include code/part1/test_pqueue_sufficiently_advanced.py -->
```

$$$NOTES

We have some methods that test correctness *in general*.

We're only specifying the kind of input, not specific values.

$$$

### How property-based tests work

* Properties are assertions about invariants. <!--@exec frag("hc")-->

* Lots of checks with randomly generated input. <!--@exec frag("hc")-->

* Failure case minimization. <!--@exec frag("hc")-->

* Focus on high-level behaviour. <!--@exec frag("hc")-->

... But no silver bullet. <!--@exec frag()-->

$$$NOTES

You like non-deterministic tests, right?

More on minimization later.

Lots of checks means lots of time.

$$$

### For real, with Hypothesis

```python
<!-- @include code/part1/test_pqueue_properties.py -->
```

$$$NOTES

This is a real test case that actually runs.
