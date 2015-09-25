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

### How we usually write tests

<br/>

```python
<!-- @include code/tests/test_deflector_tedious.py -->
```

$$$NOTES

A typical unit test suite has lots of little tests that each test one thing.

This is good, but tedious to write. People are bad at tedious things.

Focus on low-level things.

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

<span class="fragment">
...but how does `magictest` determine *correctness*?
</span>

$$$NOTES

This is the core of testing: Determining correctness.


$$$

### Maybe without the unicorns

<br/>

```python
<!-- @include code/tests/test_deflector_sufficiently_advanced.py -->
```

$$$NOTES

We have some methods that test correctness *in general*.

But we still need Sufficiently Advanced Technology to use them.


$$$

### A little less magic, perhaps

```python
<!-- @include code/tests/test_deflector_somewhat_advanced.py -->
```

$$$NOTES

This is now something we can realistically implement.

We're only specifying the kind of input, not specific values.


$$$

### For real, with Hypothesis

```python
<!-- @include code/tests/test_deflector_properties_simple.py -->
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
