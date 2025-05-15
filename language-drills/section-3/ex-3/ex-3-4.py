class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title!r})"

    def __lt__(self, other):
        return self.title < other.title


books = [Book("Zoo"), Book("1984"), Book("A Tale of Two Cities")]
sorted_books = sorted(books)
print(sorted_books)
