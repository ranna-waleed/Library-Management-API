import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/books.json')

def read_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_books(books):
    with open(DATA_FILE, 'w') as file:
        json.dump(books, file, indent=4)

class Book:
    def __init__(self, title, author, published_year, isbn, genre=None):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.isbn = isbn
        self.genre = genre

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'published_year': self.published_year,
            'isbn': self.isbn,
            'genre': self.genre
        }

    @staticmethod
    def from_dict(data):
        return Book(
            title=data['title'],
            author=data['author'],
            published_year=data['published_year'],
            isbn=data['isbn'],
            genre=data.get('genre')
        )