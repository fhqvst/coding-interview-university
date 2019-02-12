class HashMapBase(MapBase):

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)             # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)                 # subroutine maintains self._n
        if self._n > len(self._table) // 2:           # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)    # number 2^x - 1 is often prime

    def _resize(self, c):
        """Resize bucket array to capacity c and rehash all items."""
        old = list(self.items())       # use iteration to record existing items
        self._table = c * [None]       # then reset table to desired capacity
        self._n = 0                    # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v                # reinsert old key-value pair
