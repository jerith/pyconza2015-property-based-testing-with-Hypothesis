class NaivePriorityQueue(object):
    """
    A priority queue is a collection which returns items in sorted order.
    This is a naive implementation with O(N) `put()` and O(1) `get()`.
    """
    def __init__(self, items=()):
        self._items = list(items)
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def put(self, item):
        """Add an item to the collection."""
        self._items.append(item)
        self._items.sort()

    def get(self):
        """Remove and return the smallest item in the collection."""
        return self._items.pop(0)
