from hypothesis import given, strategies as st

@given(st.integers())
def test_weird_edge_case(x):
    """A number divided by itself is always 1."""
    assert (x - 1337) / (x - 1337) == 1
