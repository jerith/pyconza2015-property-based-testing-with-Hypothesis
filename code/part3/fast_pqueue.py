class FastPriorityQueue(object):
    """
    A priority queue moves the smallest item to the front.
    Heap-based implementation with O(log N) `put()` and `get()`.
    """
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def put(self, item):
        """
        Add an item to the collection.
        """
        self._heap.append(item)
        self._swim(len(self))

    def get(self):
        """
        Remove and return the smallest item in the collection.
        """
        self._swap(1, len(self))
        item = self._heap.pop()
        self._sink(1)
        return item

    def _less(self, i, j):
        """
        True if i_val and j_val exist and i_val < j_val, else False.
        """
        if max([i, j]) > len(self):
            return False
        return self._heap[i-1] < self._heap[j-1]

    def _swap(self, i, j):
        """
        Swap i_val and j_val.
        """
        self._heap[i-1], self._heap[j-1] = self._heap[j-1], self._heap[i-1]

    def _swim(self, i):
        """
        Move i_val up the heap until it's in a valid position.

        While i_val is smaller than its parent, swap with the parent.
        """
        while i > 1 and self._less(i, i/2):
            self._swap(i, i/2)
            i /= 2

    def _sink(self, i):
        """
        Move i_val down the heap until it's in a valid position.

        While i_val is larger than any children, swap with the largest child.
        """
        while i < len(self):
            j = i*2
            if self._less(j+1, j):
                j += 1
            if not self._less(j, i):
                return
            self._swap(i, j)
            i = j
