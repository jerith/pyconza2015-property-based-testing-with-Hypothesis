from hypothesis import given, strategies as st
from naive_pqueue import NaivePriorityQueue

@given(items=st.lists(st.integers()))
def test_get_all_items(items):
    """We get every item exactly once."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    while len(pq) > 0:
        items.remove(pq.get())
    assert len(items) == 0

@given(items=st.lists(st.integers(), min_size=1))
def test_get_items_in_order(items):
    """We get items in sorted order."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    current = pq.get()
    while len(pq) > 0:
        prior, current = current, pq.get()
        assert prior <= current
