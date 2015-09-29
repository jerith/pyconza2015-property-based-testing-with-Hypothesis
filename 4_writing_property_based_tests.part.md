## Part 4

<br/>
<br/>
<br/>
<br/>

### Writing property-based tests

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

### Tips for defining properties

* <span>Idempotence</span> <!--@exec frag("hc", "1")-->
  <span>*f( f(x) ) = f(x)*</span> <!--@exec frag("vhc", "1")-->

* <span>Round trip</span> <!--@exec frag("hc", "2")-->
  <span>*f<sup> -1</sup>( f(x) ) = x*</span> <!--@exec frag("vhc", "2")-->

* <span>Invariance</span> <!--@exec frag("hc", "3")-->
  <span>*g( f(x) ) = g(x)*</span> <!--@exec frag("vhc", "3")-->

* <span>Transformation</span> <!--@exec frag("hc", "4")-->
  <span>*f( g(x) ) = g'( f(x) )*</span> <!--@exec frag("vhc", "4")-->

* <span>Verification</span> <!--@exec frag("hc", "5")-->
  <span>*P( f(x) ) is true*</span> <!--@exec frag("vhc", "5")-->

* <span>Oracle</span> <!--@exec frag("hc", "6")-->
  <span>*f(x) = g(x)*</span> <!--@exec frag("vhc", "6")-->

<!--{_class="sb"}-->

$$$NOTES

Verification example: Sorted list.

An oracle assumes a known-correct implementation to test against.

$$$

### Idempotence

```python
<!-- @include code/part4/test_prop_idempotent.py -->
```

It's already been done.

$$$NOTES

$$$

### Round trip

```python
<!-- @include code/part4/test_prop_round_trip.py -->
```

There and back again.

$$$NOTES

Beware serialization differences.

$$$

### Invariance

```python
<!-- @include code/part4/test_prop_invariant.py -->
```

Some things never change.

$$$NOTES

$$$

### Transformation

```python
<!-- @include code/part4/test_prop_transformation.py -->
```

All roads lead to Rome.

$$$NOTES

$$$

### Verification

```python
<!-- @include code/part4/test_prop_verification.py -->
```

(e) None of the above.

$$$NOTES

This is true after the operation is performed.

$$$

### Oracle

```python
<!-- @include code/part4/test_prop_oracle.py -->
```

No, not the database.

$$$NOTES

Useful with a simple model or naive implementation.

$$$

### Back to our priority queue

```python
<!-- @include code/part4/naive_pqueue.py -->
```

$$$NOTES

Remember this guy? We don't want to use him in production.

$$$

### Much better priority queue

```python
<!-- @include code/part4/fast_pqueue.py -->
```

$$$NOTES

This guy is much better, but much more complex.

$$$

### Stateful tests

```python
<!-- @include code/part4/test_pqueue_stateful.py -->
```
<!--{_style="font-size:50%"}-->

$$$NOTES

We define the state machine, Hypothesis exercises it.

Show example.
