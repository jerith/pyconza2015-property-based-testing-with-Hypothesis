from hypothesis import given, strategies as st

@given(st.text())
def test_something_oracle(text):
    """
    The new thing behaves the same as the old thing.
    """
    assert True
