from book import BookV1, BookV2, save_book, load_book

# Save version 1
book_v1 = BookV1("Silent Patient", "Alex Michaelides")
save_book(book_v1, "book_v1.pkl")

# load older version
restored_book_v2 = load_book("book_v1.pkl")

print("\nRestored Book (Upgraded):")
print(restored_book_v2)

