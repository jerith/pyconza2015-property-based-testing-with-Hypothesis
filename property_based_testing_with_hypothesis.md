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

### An example


```python
<!-- @include code/deflector.py -->
```

$$$NOTES

Some simple code we want to test.

Note that the phase angle is normalised.

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

Focuses on low-level things.

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

<p class="fragment">...but how does `magictest` determine correctness?</p>

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

### For real, with Hypothesis

```python
<!-- @include code/tests/test_deflector_properties.py -->
```

$$$NOTES

This is a real test case that actually runs.

It doesn't pass, though, because float spiders.

$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
