class NaivePriorityQueue(object):
    """
    A priority queue moves the smallest item to the front.
    Naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort(reverse=True)

    def get(self):
        """Remove and return the smallest item."""
        return self._items.pop()
