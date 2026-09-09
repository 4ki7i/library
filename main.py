from library import Book, EBook, Library


def is_valid_isbn(isbn):

    return isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13)

def main():
    my_library = Library()
    b1 = Book("1984", "George Orwell", "1234567890")
    b2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "0987654321")
    eb1 = EBook("Python Crash Course", "Eric Matthes", "1111111111111", 5.2)
    eb2 = EBook("Clean Code", "Robert C. Martin", "2222222222222", 3.5)

    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(eb1)
    my_library.add_book(eb2)

    print("--- Testing Checkout and Return ---")
    my_library.checkout_book("1234567890")
    my_library.checkout_book("1234567890")
    my_library.return_book("1234567890")
    my_library.checkout_book("1111111111111") #

    print("\n--- Functional Programming: Filter (Available Books) ---")
    available_books = my_library.list_available_books()
    for book in available_books:
        print(book.__str__())

    print("\n--- Functional Programming: Sorted (Alphabetical) ---")
    all_books = my_library.get_all_books()
    sorted_books = sorted(all_books, key=lambda b: b.title)
    for book in sorted_books:
        print(f"- {book.title}")

    print("\n--- Functional Programming: Map (Titles Only) ---")
    book_titles = list(map(lambda b: b.title, all_books))
    print(book_titles)

    print("\n--- Testing Standalone Function: is_valid_isbn ---")
    print(f"Is '1234567890' valid? {is_valid_isbn('1234567890')}")
    print(f"Is '123ABCD' valid? {is_valid_isbn('123ABCD')}")

if __name__ == "__main__":
    main()
