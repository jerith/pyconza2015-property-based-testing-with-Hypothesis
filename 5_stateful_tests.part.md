## Part 5

<br/>
<br/>
<br/>
<br/>

### Stateful tests

$$$

### Back to our priority queue

```python
<!-- @include code/part5/naive_pqueue.py -->
```

$$$NOTES

Remember this guy? We don't want to use him in production.

$$$

### Much better priority queue

```python
<!-- @include code/part5/fast_pqueue.py -->
```

$$$NOTES

This guy is much better, but much more complex.

$$$

### Priority queue stateful tests

```python
<!-- @include code/part5/test_pqueue_stateful.py -->
```
<!--{_style="font-size:50%"}-->

$$$NOTES

We define the state machine, Hypothesis exercises it.

$$$

### Failure report

If we use `max` instead of `min` in the test, it fails:

```pytestresult
<!-- @include code/part5/failtest_pqueue_stateful.out -->
```

We get a minimized<sup>*</sup> failing sequence of operations.

<br/><sup>*</sup><small>but not necessarily minimal</small>

$$$NOTES

This kind of thing is really hard to minimize, but Hypothesis does pretty well.
