from hypothesis import given, strategies as st
from naive_pqueue import NaivePriorityQueue

@given(items=st.lists(st.integers(), min_size=1))
def test_items_are_returned_in_priority_order(items):
    """We always get the smallest item first."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    assert len(pq) == len(items)
    current = pq.get()
    while len(pq) > 0:
        prior, current = current, pq.get()
        assert prior <= current

@given(items=st.lists(st.integers()))
def test_all_items_are_returned_exactly_once(items):
    """We always get every item exactly once."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    assert len(pq) == len(items)
    while len(pq) > 0:
        items.remove(pq.get())
    assert len(items) == 0
