class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("And then there were none", "Agatha Christie")
print(b.title,"by", b.author)
