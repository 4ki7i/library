class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} (Physical Book)"

class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb):
        super().__init__(title, author, isbn)
        self.file_size_mb = file_size_mb
    def __str__  (self):
        return f"'{self.title}' by {self.author} (E-Book, {self.file_size_mb}MB)"

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def find_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.__books.remove(book)

    def checkout_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"Success: '{book.title}' has been checked out.")
            else:
                print(f"Error: '{book.title}' is already checked out.")
        else:
            print(f"Error: Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            book.is_available = True
            print(f"Success: '{book.title}' has been returned.")
        else:
            print(f"Error: Book with ISBN {isbn} not found.")

    def list_available_books(self):
        return list(filter(lambda b: b.is_available, self.__books))

    def get_all_books(self):
        return self.__books