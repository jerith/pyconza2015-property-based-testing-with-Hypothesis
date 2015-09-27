from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sum_less_than_42(numbers):
    assert sum(numbers) < 42
