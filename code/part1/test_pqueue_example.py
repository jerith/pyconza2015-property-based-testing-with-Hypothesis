from naive_pqueue import NaivePriorityQueue

def mkpq(items):
    """Create and fill a NaivePriorityQueue."""
    pq = NaivePriorityQueue()
    [pq.put(item) for item in items]
    return pq

def test_get_only():
    """If there's only one item, we get that."""
    pq = mkpq(["a"])
    assert pq.get() == "a"
    assert len(pq) == 0

def test_get_both():
    """If there are two items, we get both in order."""
    pq = mkpq(["a", "b"])
    assert pq.get() == "a"
    assert pq.get() == "b"
    assert len(pq) == 0

def test_put_only():
    """If the queue is empty, putting is trivial."""
    pq = NaivePriorityQueue()
    pq.put("a")
    assert pq._items == ["a"]

def test_put_small():
    """If we put a small item, it lands at the front."""
    pq = mkpq(["b", "c"])
    pq.put("a")
    assert pq._items == ["a", "b", "c"]

def test_put_big():
    """If we put a big item, it lands at the back."""
    pq = mkpq(["a", "b"])
    pq.put("c")
    assert pq._items == ["a", "b", "c"]

# And many more that I didn't write because I got bored and
# wandered off to work on something more interesting or play
# videogames or eat lunch.
