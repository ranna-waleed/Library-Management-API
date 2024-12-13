import json

class Book:
    def __init__(self, title, author, published_year, isbn, genre=None):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.isbn = isbn
        self.genre = genre

    def to_dict(self):
        return self.__dict__

def load_books():
    try:
        with open('data/books.json', 'r') as file:
            books_data = json.load(file)
            return [Book(**book) for book in books_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_books(books):
    with open('data/books.json', 'w') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)