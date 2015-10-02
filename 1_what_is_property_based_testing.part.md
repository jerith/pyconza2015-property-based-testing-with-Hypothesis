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

### Defining correctness

Let's define "correctness" for a priority queue.

```python
<!-- @include code/part1/prop_priority.py -->
```
<!--@exec frag()-->

```python
<!-- @include code/part1/prop_queue.py -->
```
<!--@exec frag()-->

$$$NOTES

We have some functions that test correctness *in general*.

Taken together, they describe what it is to be a priority queue.

$$$

### How property-based tests work

* Focus on high-level requirements. <!--@exec frag("hc")-->

* Properties define behaviour. <!--@exec frag("hc")-->

* Randomly generated input. <!--@exec frag("hc")-->

* Failure case minimization. <!--@exec frag("hc")-->

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
<!--{_style="font-size:55%"}-->

$$$NOTES

This is a real test case that actually runs.

Doesn't say anything about order of operations.
