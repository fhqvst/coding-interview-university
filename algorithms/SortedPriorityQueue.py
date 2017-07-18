class SortedPriorityQueue():
    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
          self._key = k
          self._value = v

        def __lt__(self, other):
          return self._key < other._key    # compare items based on their keys

        def __repr__(self):
          return '({0},{1})'.format(self._key, self._value)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        item = self._Item(key, value)
        if self.is_empty():
            self._data.append(item)
        else:
            i = 0
            while i < len(self._data) and self._data[i]._key < key:
                i += 1
            self._data = self._data[0:i] + [item] + self._data[i:]

    def min(self):
        # should check if empty as well
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        # should check if empty as well
        item = self._data[0]
        del self._data[0:1]
        return (item._key, item._value)

pq = SortedPriorityQueue()
pq.add(3,'A')
pq.add(5,'B')
pq.add(4,'C')
pq.add(2,'D')
pq.add(1,'E')

assert len(pq) == 5
assert pq.min() == (1,'E')
assert pq.remove_min() == (1,'E')
assert pq.remove_min() == (2,'D')
assert pq.remove_min() == (3,'A')
assert len(pq) == 2
assert pq.remove_min() == (4,'C')
assert pq.remove_min() == (5,'B')
