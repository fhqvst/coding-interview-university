class ReversedSequenceIterator():

    def __init__(self, sequence):
        self.__sequence = sequence
        self.__i = len(sequence)

    def __next__(self):
        self.__i -= 1
        if self.__i >= 0 :
            return self.__sequence[self.__i]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

if __name__ == '__main__':
    i = 5
    for k in ReversedSequenceIterator([1,2,3,4,5]):
        assert i == k
        i -= 1
