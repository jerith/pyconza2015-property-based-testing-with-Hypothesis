from hypothesis import given, example, strategies as st

@example(1337)
@given(st.integers())
def test_weird_edge_case(x):
    """A number divided by itself is always 1, right?"""
    assert (x - 1337) / (x - 1337) == 1
