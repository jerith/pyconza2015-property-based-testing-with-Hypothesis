def items_are_returned_in_priority_order(pq, items):
    """We always get the smallest item first."""
    for item in items:
        pq.put(item)
    assert len(pq) == len(items)
    current = pq.get()
    while len(pq) > 0:
        prior, current = current, pq.get()
        assert prior <= current
