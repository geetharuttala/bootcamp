class Library:
    def __init__(self):
        self.books = ["1984", "Sapiens", "Dune"]

    def __getitem__(self, index):
        return self.books[index]


lib = Library()
print(lib[0])
print(lib[2])
