class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            val = self.current
            self.current += 1
            return val
        raise StopIteration

for i in Counter(3):
    print(i)
