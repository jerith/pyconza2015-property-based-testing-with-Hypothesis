import math
from hypothesis import given, strategies as st

@given(st.floats().filter(lambda x: not math.isnan(x)))
def test_additive_inverse_float(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)
