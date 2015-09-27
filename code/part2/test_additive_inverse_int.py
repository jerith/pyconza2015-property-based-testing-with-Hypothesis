from hypothesis import given, strategies as st

@given(st.integers())
def test_additive_inverse_int(x):
    """Double additive inverse has no effect."""
    assert x == -(-x)
