import math
from hypothesis import given, assume, strategies as st

@given(st.floats())
def test_additive_inverse_float(x):
    """Double additive inverse has no effect (except NaN)."""
    assume(not math.isnan(x))
    assert x == -(-x)
