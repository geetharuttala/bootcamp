class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

    def __eq__(self, other):
        return isinstance(other, Book) and (self.title, self.author) == (other.title, other.author)

print(Book("And then there were none", "Agatha Christie") == Book("1984", "Orwell"))
print(Book("1984", "Orwell") == Book("1984", "Orwell"))
