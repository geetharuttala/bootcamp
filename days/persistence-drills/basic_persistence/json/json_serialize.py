import json

class Book:
    def __init__(self, title: str, author: str, year: int, genres: list[str]):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres

    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=4)

book = Book(
    title="Verity",
    author="Colleen Hoover",
    year=2018,
    genres=["Thriller", "Psychological  thriller"]
)

book_json = book.to_json()
print("Serialized JSON string:")
print(book_json)