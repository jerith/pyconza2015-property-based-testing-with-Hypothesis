## Part 3

<br/>
<br/>
<br/>
<br/>

### Stateful testing

$$$

### Managing generated input <span style="opacity: 0.3">(1)</span>

Additive inverse (integers)

```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_additive_inverse_int(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)

```

```pytestresult
========================= test session starts ==========================
test_additive_inverse_int.py .
======================= 1 passed in 0.13 seconds =======================

```
<!--{_class="fragment"}-->

$$$NOTES

Very simple example, valid for all integers.
