from hypothesis import given, strategies as st

@given(number=st.floats(-1e300, 1e300), decimals=st.integers(0, 5))
def test_round_idempotent(number, decimals):
    """
    Rounding an already-rounded number is a no-op.
    """
    rounded = round(number, decimals)
    assert rounded == round(rounded, decimals)
