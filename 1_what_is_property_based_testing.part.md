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
<!-- @include code/deflector.py -->
```

$$$NOTES

Some simple code we want to test.

Note that the phase angle is normalised.

Degrees instead of radians to avoid some spiders.

$$$

### How we usually write tests

```python
<!-- @include code/tests/test_deflector_tedious.py -->
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
<!-- @include code/tests/test_deflector_magic.py -->
```
<!-- {_class="fragment"} -->

<br/>

<p class="fragment">...but how does `magictest` know what "correct" is?</p>

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
<!-- @include code/tests/test_deflector_sufficiently_advanced.py -->
```

$$$NOTES

We have some methods that test correctness *in general*.

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
<!-- @include code/tests/test_deflector_properties.py -->
```

$$$NOTES

This is a real test case that actually runs.

Floating point approximation spiders.
