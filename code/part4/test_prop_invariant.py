from hypothesis import given, strategies as st

@given(st.randoms(), st.lists(st.integers()))
def test_something_invariant(rand, items):
    """
    The set of items in a collection does not change when shuffling.
    """
    orig_items = list(items)
    rand.shuffle(items)
    for item in items:
        orig_items.remove(item)
    assert orig_items == []
