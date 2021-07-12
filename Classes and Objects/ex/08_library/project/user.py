class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books.keys():
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in library.rented_books.items():
            for b_n, days in data.items():
                if b_n == book_name:
                    return f"The book \"{book_name}\" is already rented and will be available in {days} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.rented_books[self.username].pop(book_name)
        library.books_available[author].append(book_name)
        self.books.remove(book_name)

    def info(self):
        self.books.sort()
        return ", ".join(self.books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
