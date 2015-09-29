## Part 4

<br/>
<br/>
<br/>
<br/>

### Writing properties

$$$

### What makes a good property?

* True for (almost) all input. <!--@exec frag("hc")-->

* Does not duplicate the code under test. <!--@exec frag("hc")-->

* Describes the code under test in a meaningful way. <!--@exec frag("hc")-->

* Not too expensive to check. <!--@exec frag("hc")-->

Harder than example-based tests, but a lot more useful. <!--@exec frag()-->

$$$NOTES

Well-defined exceptions are okay, but test separately.

You'll be running these hundreds of times.

$$$

### Idempotence

*f( f(x) ) = f(x)*

```python
<!-- @include code/part4/test_prop_idempotent.py -->
```
<!--@exec frag("", "1")-->

It's already been done.
<!--@exec frag("", "1")-->

$$$NOTES

$$$

### Round trip

*f<sup> -1</sup>( f(x) ) = x*

```python
<!-- @include code/part4/test_prop_round_trip.py -->
```
<!--@exec frag("", "1")-->

There and back again.
<!--@exec frag("", "1")-->

$$$NOTES

Beware serialization differences.

$$$

### Invariance

*g( f(x) ) = g(x)*

```python
<!-- @include code/part4/test_prop_invariant.py -->
```
<!--@exec frag("", "1")-->

Some things never change.
<!--@exec frag("", "1")-->

$$$NOTES

$$$

### Transformation

*f( g(x) ) = g'( f(x) )*

```python
<!-- @include code/part4/test_prop_transformation.py -->
```
<!--@exec frag("", "1")-->

All roads lead to Rome.
<!--@exec frag("", "1")-->

$$$NOTES

$$$

### Verification

*P( f(x) ) is true*

```python
<!-- @include code/part4/test_prop_verification.py -->
```
<!--@exec frag("", "1")-->

(e) None of the above.
<!--@exec frag("", "1")-->

$$$NOTES

This is true after the operation is performed.

$$$

### Oracle

*f(x) = g(x)*

```python
<!-- @include code/part4/test_prop_oracle.py -->
```
<!--@exec frag("", "1")-->

No, not the database.
<!--@exec frag("", "1")-->

$$$NOTES

Useful with a simple model or naive implementation.
