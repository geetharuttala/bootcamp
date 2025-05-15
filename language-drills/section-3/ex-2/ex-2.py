# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Subclassing
class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {super().describe()} (Genre: {self.genre})"


# Multiple Inheritance
class AudioMixin:
    def play_audio(self):
        print(f"Playing audio for: {self.title}")


class AudioBook(Book, AudioMixin):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration


# Tests

# Create Novel
novel = Novel("Dune", "Frank Herbert", "Sci-Fi")
print(novel.describe())  # Overridden describe()
print("Genre:", novel.genre)

# Check __str__
book = Book("1984", "Orwell")
print(str(book))  # Uses __str__

# AudioBook test
ab = AudioBook("Sapiens", "Yuval Noah Harari", "15h")
ab.play_audio()

# isinstance test
print("Is Novel a Book?", isinstance(novel, Book))

# Polymorphism in action
library = [book, novel]
for item in library:
    print(item.describe())
