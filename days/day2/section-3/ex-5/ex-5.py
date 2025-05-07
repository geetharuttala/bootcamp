from dataclasses import dataclass
import json

@dataclass
class Book:
    title: str
    author: str

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        return isbn.isdigit() and len(isbn) in (10, 13)

    @classmethod
    def from_string(cls, s: str):
        title, author = s.split("|")
        return cls(title.strip(), author.strip())

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["title"], d["author"])

    @classmethod
    def from_json(cls, s: str):
        d = json.loads(s)
        return cls.from_dict(d)

    def describe(self):
        return f"{self.title} by {self.author}"


# Subclass to test cls behavior
class Novel(Book):
    def describe(self):
        return f"Novel: {super().describe()}"

    @classmethod
    def from_string(cls, s: str):  # Overridden classmethod
        print("Using Novel.from_string")
        return super().from_string(s)


# Test cases
print("Static method from class:", Book.is_valid_isbn("1234567890"))         # True
b = Book("1984", "Orwell")
print("Static method from instance:", b.is_valid_isbn("not-an-isbn"))        # False

book1 = Book.from_string("Dune | Frank Herbert")
print("From string:", book1.describe())

book2 = Book.from_dict({"title": "Sapiens", "author": "Yuval Noah Harari"})
print("From dict:", book2.describe())

book3 = Book.from_json('{"title": "The Alchemist", "author": "Paulo Coelho"}')
print("From JSON:", book3.describe())

# Using classmethod with subclass
novel = Novel.from_string("Brave New World | Aldous Huxley")
print("Novel from_string:", novel.describe())
print("Type of novel:", type(novel).__name__)  # Should be Novel

# Demonstrate method resolution
print("Is Novel.from_string overridden?", Novel.from_string is not Book.from_string)

# Example where static, class, and instance methods are all useful
print("\n--- Hybrid Use Case ---")
class LibraryUtils:
    @staticmethod
    def clean_title(title: str) -> str:
        return title.title().strip()

    @classmethod
    def create_book(cls, raw_title: str, author: str):
        return Book(cls.clean_title(raw_title), author)

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

lib = LibraryUtils()
book_clean = LibraryUtils.create_book("   the art of war   ", "Sun Tzu")
lib.add_book(book_clean)
print(lib.books[0])
