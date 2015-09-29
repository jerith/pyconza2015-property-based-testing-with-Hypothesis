from hypothesis import given, strategies as st

@given(st.floats())
def test_additive_inverse_float(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)
