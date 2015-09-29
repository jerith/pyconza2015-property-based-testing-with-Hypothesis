from sufficiently_advanced_technology import CorrectnessDefinition, number_list
from naive_pqueue import NaivePriorityQueue

class PriorityQueueCorrectnessDefinition(CorrectnessDefinition):

    def get_items_in_priority_order(self, items=number_list):
        """Priority: we always get the smallest item first."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        current = pq.get()
        while len(pq) > 0:
            prior, current = current, pq.get()
            assert prior <= current

    def get_all_items(self, items=number_list):
        """Queue: we always get every item exactly once."""
        pq = NaivePriorityQueue()
        [pq.put(item) for item in items]
        while len(pq) > 0:
            items.remove(pq.get())
        assert len(items) == 0

PriorityQueueCorrectnessDefinition.assert_correct()
