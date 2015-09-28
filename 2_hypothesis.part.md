## Part 2

<br/>
<br/>
<br/>
<br/>

### Hypothesis basics

$$$

### Strategies

A strategy is a set of rules:

* It knows how to generate values. <!--@exec frag("hc", "1")-->
  *(Of course.)* <!-- @exec frag("vhc", "1") -->

* It knows how to simplify values. <!--@exec frag("hc", "2")-->
  *(Very important!)* <!--@exec frag("vhc", "2")-->

* It's composable. <!--@exec frag("hc", "3")-->
  *(Building blocks for complex data.)* <!--@exec frag("vhc", "3")-->


Built-in strategies are very clever, so yours can be simple.
<!--@exec frag()-->

$$$NOTES

Other tools call them generators.

.example() generates a random example.

$$$

### Managing generated input <span style="opacity: 0.3">(1)</span>

Additive inverse (integers)

```python
<!-- @include code/part2/test_additive_inverse_int.py -->
```

```pytestresult
<!-- @include code/part2/test_additive_inverse_int.out -->
```
<!--@exec frag()-->

$$$NOTES

Very simple example, valid for all integers.

$$$

### Managing generated input <span style="opacity: 0.3">(2)</span>

Additive inverse (floating point)

```python
<!-- @include code/part2/failtest_additive_inverse_float.py -->
```

```pytestresult
<!-- @include code/part2/failtest_additive_inverse_float.out -->
```
<!--@exec frag()-->

$$$NOTES

Fails because `NaN` is not equal to anything.

$$$

### Managing generated input <span style="opacity: 0.3">(3)</span>

Additive inverse (floating point) without NaN

```python
<!-- @include code/part2/test_additive_inverse_float.py -->
```

```pytestresult
<!-- @include code/part2/test_additive_inverse_float.out -->
```
<!--@exec frag()-->

$$$NOTES

`assume()` tells Hypothesis to ignore this example.

$$$

### Managing generated input <span style="opacity: 0.3">(4)</span>

```python
<!-- @include code/part2/test_weird_edge_case.py -->
```

Note the potential division by zero.

```pytestresult
<!-- @include code/part2/test_weird_edge_case.out -->
```
<!--@exec frag()-->

$$$NOTES

Random generation doesn't find everything.

Built-in strategies are cleverly weighted to include common edge cases.

$$$

### Managing generated input <span style="opacity: 0.3">(5)</span>

```python
<!-- @include code/part2/failtest_weird_edge_case.py -->
```

We explicitly include the divide-by-zero input.

```pytestresult
<!-- @include code/part2/failtest_weird_edge_case.out -->
```
<!--@exec frag()-->

$$$NOTES

Random generation doesn't find everything.

Built-in strategies are cleverly weighted to include common edge cases.

$$$

### Strategies: combinations

ints or floats or strings:

```python
<!-- @include demos/ints_or_floats_or_strings.txt -->
```

Beware: `text()|none()` ⇒ half strings, half `None`.

<!--@exec frag("", "1")-->

$$$NOTES

Sometimes you want to choose from multiple strategies.

$$$

### Strategies: filter and map

Lists with even lengths:

```python
<!-- @include demos/even_lists.txt -->
```

Odd integers:
<!--@exec frag("", "1")-->

```python
<!-- @include demos/odd_integers.txt -->
```
<!--@exec frag("", "1")-->

$$$NOTES

Filter predicates mustn't be too hard to satisfy.

Use map instead of filter where possible.

$$$

### Strategies: flatmap

Square text:

```python
<!-- @include code/part2/square_text.py -->
```

```python
<!-- @include demos/square_text.txt -->
```

$$$NOTES

You probably won't use this much.

$$$

### Strategies: recursive

Nested dicts:

```python
<!-- @include demos/nested_dicts.txt -->
```

$$$NOTES

This stuff is in the docs.

$$$

### Minimization <span style="opacity: 0.3">(1)</span>

```python
<!-- @include code/part2/failtest_minimization.py -->
```

```pytestresult
<!-- @include code/part2/failtest_minimization.out -->
```
<!--@exec frag()-->

The falsifying example is the simplest failing input.
<!--@exec frag()-->

$$$NOTES

What witchcraft is this!?

Minimization filters out the noise of random input.

$$$

### Minimization <span style="opacity: 0.3">(2)</span>

```python
<!-- @include code/part2/failtest_minimization_nontrivial.py -->
```

```pytestresult
<!-- @include code/part2/failtest_minimization_nontrivial.out -->
```

Works for more complicated cases as well.

$$$NOTES

Not perfect. Sometimes non-minimal data gets through.
