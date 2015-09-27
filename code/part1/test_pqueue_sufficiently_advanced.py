from sufficiently_advanced_technology import VerifyCorrect, number_list
from naive_pqueue import NaivePriorityQueue

class VerifyPriorityQueueCorrect(VerifyCorrect):
    def get_all_items(self, items=number_list):
        """We get every item exactly once."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        while len(pq) > 0:
            items.remove(pq.get())
        assert len(items) == 0

    def get_items_in_order(self, items=number_list):
        """We get items in sorted order."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        prior = current = pq.get()
        while len(pq) > 0:
            prior, current = current, pq.get()
            assert prior <= current

VerifyPriorityQueueCorrect.assert_correct()
