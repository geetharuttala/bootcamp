class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)


lib = Library()
lib.add_book("1984")
lib.add_book("Sapiens")
print(len(lib))
