from hypothesis import given, strategies as st
from random import shuffle

@given(st.lists(st.integers()))
def test_something_invariant(items):
    """
    The set of items in a collection does not change when shuffling.
    """
    orig_items = list(items)
    shuffle(items)
    for item in items:
        orig_items.remove(item)
    assert orig_items == []
