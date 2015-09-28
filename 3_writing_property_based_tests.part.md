## Part 3

<br/>
<br/>
<br/>
<br/>

### Writing property-based tests

$$$

### What makes a good property?

* True for (almost) all input.

* Does not duplicate the code under test.

* Describes the code under test in a meaningful way.

* Not too expensive to check.

Harder than writing example-based tests, but a lot more useful.
<!--@exec frag()-->


$$$NOTES

Well-defined exceptions are okay, but test separately.

You'll be running these hundreds of times.

$$$

### Tips for defining properties

* <span>Idempotence</span> <!--@exec frag("hc hblock", "1")-->
  <span>*f( f(x) ) = f(x)*</span> <!--@exec frag("vhc hblock", "1")-->

* <span>Round trip</span> <!--@exec frag("hc hblock", "2")-->
  <span>*f<sup> -1</sup>( f(x) ) = x*</span> <!--@exec frag("vhc hblock", "2")-->

* <span>Invariant</span> <!--@exec frag("hc hblock", "3")-->
  <span>*g( f(x) ) = g(x)*</span> <!--@exec frag("vhc hblock", "3")-->

* <span>Transformation</span> <!--@exec frag("hc hblock", "4")-->
  <span>*f( g(x) ) = g'( f(x) )*</span> <!--@exec frag("vhc hblock", "4")-->

* <span>Verification</span> <!--@exec frag("hc hblock", "5")-->
  <span>*P( f(x) ) is true*</span> <!--@exec frag("vhc hblock", "5")-->

* <span>Oracle</span> <!--@exec frag("hc hblock", "6")-->
  <span>*f(x) = g(x)*</span> <!--@exec frag("vhc hblock", "6")-->

<!--{_style="width: 16em"}-->

$$$NOTES

Verification example: Sorted list.

An oracle assumes a known-correct implementation to test against.

$$$

### Idempotent property

```python
<!-- @include code/part3/test_prop_idempotent.py -->
```

$$$NOTES

Pretty straightforward. Might be slow.

$$$

### Round trip property

```python
<!-- @include code/part3/test_prop_round_trip.py -->
```

$$$NOTES

Beware serialization differences.

$$$

### Invariant property

```python
<!-- @include code/part3/test_prop_invariant.py -->
```

$$$NOTES

$$$

### Transformation property

```python
<!-- @include code/part3/test_prop_transformation.py -->
```

$$$NOTES

$$$

### Verification property

```python
<!-- @include code/part3/test_prop_verification.py -->
```

$$$NOTES

$$$

### Oracle property

```python
<!-- @include code/part3/test_prop_oracle.py -->
```

$$$NOTES

$$$

### Back to our priority queue

```python
<!-- @include code/part3/naive_pqueue.py -->
```

$$$NOTES

Remember this guy? We don't want to use him in production.

$$$

### Much better priority queue

```python
<!-- @include code/part3/fast_pqueue.py -->
```

$$$NOTES

This guy is much better, but much more complex.

$$$

### Stateful test

```python
<!-- @include code/part3/test_pqueue_stateful.py -->
```
<!--{_style="font-size:50%"}-->

$$$NOTES

This guy is much better, but much more complex.
