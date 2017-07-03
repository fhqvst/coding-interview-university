class TowersOfHanoi:
    def __init__(self, size = 4):
        self.size = size
        self.a = Pin([ i + 1 for i in range(self.size) ])
        self.b = Pin()
        self.c = Pin()

    def solve(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print('Solving...')
        calls = self._solve(self.a, self.b, self.c, self.size)
        print(self.a)
        print(self.b)
        print(self.c)
        print('Calls made: ' + str(calls))

    def _move(self, from_pin, to_pin):
        to_pin.push(from_pin.pop())

    def _solve(self, from_pin, temp_pin, to_pin, size):
        if size == 1:
            self._move(from_pin, to_pin)
            return 1
        else:
            calls = 0

            # Move every disc but the last to temp_pin
            calls += self._solve(from_pin, to_pin, temp_pin, size - 1)

            # Move the the last disc to to_pin
            self._move(from_pin, to_pin)
            calls += 1

            # Move remaining discs to to_pin
            calls += self._solve(temp_pin, from_pin, to_pin, size - 1)

            return calls

class Pin:
    def __init__(self, stack = []):
        self.stack = stack

    def push(self, item):
        if (len(self.stack)) and self.stack[0] < item:
            raise Exception("You may not place a larger disc on top of a smaller disc.")
        self.stack = [item] + self.stack

    def pop(self):
        if len(self.stack) == 0: return None
        return self.stack.pop(0)

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


TowersOfHanoi(31).solve()
