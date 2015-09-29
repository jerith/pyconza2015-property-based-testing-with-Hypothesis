## Part 2

<br/>
<br/>
<br/>
<br/>

### Generating values

$$$

### Strategies

A strategy is a set of rules:

* It knows how to generate values. <!--@exec frag("hc", "1")-->
  *(Of course.)* <!-- @exec frag("vhc", "1") -->

* It knows how to simplify values. <!--@exec frag("hc", "2")-->
  *(Very important!)* <!--@exec frag("vhc", "2")-->

* It's composable. <!--@exec frag("hc", "3")-->
  *(Building blocks for complex data.)* <!--@exec frag("vhc", "3")-->

Built-in strategies are very clever so yours can be simple.
<!--@exec frag()-->

$$$NOTES

Other tools call them generators.

Django models, too.

$$$

### Excluding values

Additive inverse

```python
<!-- @include code/part2/failtest_additive_inverse_nan.py -->
```

```pytestresult
<!-- @include code/part2/failtest_additive_inverse_nan.out -->
```
<!--@exec frag()-->

$$$NOTES

Fails because `NaN` is not equal to anything.

$$$

### Excluding values: assume

Additive inverse assuming no NaN

```python
<!-- @include code/part2/test_additive_inverse_assume.py -->
```

```pytestresult
<!-- @include code/part2/test_additive_inverse_assume.out -->
```

$$$NOTES

`assume()` tells Hypothesis to ignore this example.

$$$

### Excluding values: filter

Additive inverse filtering NaN

```python
<!-- @include code/part2/test_additive_inverse_filter.py -->
```

```pytestresult
<!-- @include code/part2/test_additive_inverse_filter.out -->
```

$$$NOTES

`assume()` tells Hypothesis to ignore this example.

$$$

### Including values

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

### Including values: @example

```python
<!-- @include code/part2/failtest_weird_edge_case.py -->
```

We explicitly include the divide-by-zero input.

```pytestresult
<!-- @include code/part2/failtest_weird_edge_case.out -->
```

$$$NOTES

Hypothesis tracks failing examples, but that doesn't work for CI.

$$$

### Building strategies

* <span>Multiple strategies</span><!--@exec frag("hc", "1")-->
  <span>`st.text()|st.none()`</span><!--@exec frag("", "1")-->

* <span>Modifications</span><!--@exec frag("hc", "2")-->
  <span>`.map()` and `.filter()`</span><!--@exec frag("", "2")-->

* <span>New things</span><!--@exec frag("hc", "3")-->
  <span>`.flatmap()` and `recursive()`</span><!--@exec frag("", "3")-->

* <span>Build from scratch</span><!--@exec frag("hc", "4")-->

<!--{_class="sb"}-->

$$$NOTES

Half strings, half `None`.

See docs for details.

$$$

### flatmap: square text

```python
<!-- @include code/part2/square_text.py -->
```

```python
<!-- @include code/part2/square_text.txt -->
```

$$$NOTES

You probably won't use this much.

$$$

### recursive: nested dicts

```python
<!-- @include code/part2/nested_dicts.py -->
```

```python
<!-- @include code/part2/nested_dicts.txt -->
```

$$$NOTES

This stuff is in the docs.

$$$

### Minimization

```python
<!-- @include code/part2/failtest_minimization.py -->
```

```pytestresult
<!-- @include code/part2/failtest_minimization.out -->
```
<!--@exec frag()-->

The example is (usually) the simplest failing input.
<!--@exec frag()-->

$$$NOTES

What witchcraft is this!?

Minimization filters out the noise of random input.

$$$

### More minimization

```python
<!-- @include code/part2/failtest_minimization_nontrivial.py -->
```

```pytestresult
<!-- @include code/part2/failtest_minimization_nontrivial.out -->
```

Works for more complicated cases as well.

$$$NOTES

Not perfect. Sometimes non-minimal data gets through.
