from hypothesis import assume, strategies as st
from hypothesis.stateful import RuleBasedStateMachine, rule
from fast_pqueue import FastPriorityQueue

class PriorityQueueStateMachine(RuleBasedStateMachine):
    def __init__(self):
        super(PriorityQueueStateMachine, self).__init__()
        self.items = []
        self.pq = FastPriorityQueue()

    @rule(item=st.integers())
    def check_put(self, item):
        assert len(self.pq) == len(self.items)
        self.pq.put(item)
        self.items.append(item)

    @rule()
    def check_get(self):
        assert len(self.pq) == len(self.items)
        assume(len(self.items) > 0)
        item = max(self.items)
        self.items.remove(item)
        got = self.pq.get()
        assert got == item

TestPriorityQueue = PriorityQueueStateMachine.TestCase
