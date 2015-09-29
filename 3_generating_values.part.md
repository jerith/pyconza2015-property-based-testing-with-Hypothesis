## Part 3

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

### Simple strategies

```python
<!-- @include code/part3/just.txt -->
```

```python
<!-- @include code/part3/text_or_none.txt -->
```
<!--@exec frag()-->

```python
<!-- @include code/part3/tuples.txt -->
```
<!--@exec frag()-->

```python
<!-- @include code/part3/powers_of_two.txt -->
```
<!--@exec frag()-->

$$$NOTES

Beware duplicates when combining strategies.

$$$

### flatmap: square text

```python
<!-- @include code/part3/square_text.py -->
```

```python
<!-- @include code/part3/square_text.txt -->
```

$$$NOTES

You probably won't use this much.

$$$

### recursive: nested dicts

```python
<!-- @include code/part3/nested_dicts.py -->
```

```python
<!-- @include code/part3/nested_dicts.txt -->
```

$$$NOTES

This stuff is in the docs.
