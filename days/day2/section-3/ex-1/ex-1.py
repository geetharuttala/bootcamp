class Book:
    category = "Fiction"  # Class variable

    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

    def update_title(self, new_title):
        self.title = new_title


# Create an Object and print attributes
book1 = Book("And then there were none", "Agatha Christie")
print("Title:", book1.title)
print("Author:", book1.author)

# Call describe()
print("Describe:", book1.describe())

# Print class variable
print("Category:", book1.category)

# Update title
book1.update_title("Animal Farm")
print("Updated title:", book1.title)

# Create with default constructor
book2 = Book()
print("Default describe:", book2.describe())

# Add dynamic attribute
book1.publisher = "Secker & Warburg"
print("Publisher:", book1.publisher)

# Check type
print("Is book1 a Book?", isinstance(book1, Book))
