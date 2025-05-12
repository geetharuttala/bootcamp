import json

class Book:
    def __init__(self, title: str, author: str, year: int, genres: list[str]):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres

    @classmethod
    def from_json(cls, json_string: str) -> "Book":
        data = json.loads(json_string)
        return cls(**data)

book_json = '''
{
    "title": "Verity",
    "author": "Colleen Hoover",
    "year": 2018,
    "genres": [
        "Thriller",
        "Psychological  thriller"
    ]
}
'''

book = Book.from_json(book_json)

print("Deserialized Book object:")
print(vars(book))