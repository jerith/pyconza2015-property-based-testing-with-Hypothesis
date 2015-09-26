from hypothesis import given, strategies as st


@given(st.integers())
def test_addition_identity(x):
    assert x + 0 == x


@given(st.integers(), st.integers())
def test_addition_commutative(x, y):
    assert x + y == y + x


@given(st.integers(), st.integers(), st.integers())
def test_addition_associative(x, y, z):
    assert (x + y) + z == x + (y + z)
