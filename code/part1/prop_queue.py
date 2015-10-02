def all_items_are_returned_exactly_once(pq, items):
    """We always get every item exactly once."""
    for item in items:
        pq.put(item)
    assert len(pq) == len(items)
    while len(pq) > 0:
        items.remove(pq.get())
    assert len(items) == 0
