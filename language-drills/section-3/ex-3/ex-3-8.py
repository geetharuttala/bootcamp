class Container:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return bool(self.items)


c1 = Container([1, 2, 3])
c2 = Container([])

print(bool(c1))
print(bool(c2))
