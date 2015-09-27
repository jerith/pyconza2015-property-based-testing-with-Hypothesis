from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sum_less_than_42_nontrivial(numbers):
    if len(numbers) > 2:
        assert sum(numbers) < 42
