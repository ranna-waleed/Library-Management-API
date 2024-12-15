import json
from flask import request, jsonify
from src.models.book import Book
import os

books_file_path = os.path.join(os.path.dirname(__file__), '../data/books.json')

def get_books():
    with open(books_file_path, 'r') as file:
        return json.load(file)

def save_books(books):
    with open(books_file_path, 'w') as file:
        json.dump(books, file, indent=2)

def add_book():
    books = get_books()
    new_book = request.get_json()
    books.append(new_book)
    save_books(books)
    return jsonify({'message': 'Book added successfully'}), 200

def list_books():
    books = get_books()
    return jsonify(books), 200

def search_books():
    author = request.args.get('author')
    published_year = request.args.get('publishedYear')
    genre = request.args.get('genre')
    books = get_books()

    if author:
        books = [book for book in books if book['author'] == author]
    if published_year:
        books = [book for book in books if book['published_year'] == int(published_year)]
    if genre:
        books = [book for book in books if book['genre'] == genre]

    return jsonify(books), 200

def delete_book(isbn):
    books = get_books()
    books = [book for book in books if book['isbn'] != isbn]
    save_books(books)
    return jsonify({'message': 'Book deleted successfully'}), 200

def update_book(isbn):
    updated_book = request.get_json()
    books = get_books()
    books = [updated_book if book['isbn'] == isbn else book for book in books]
    save_books(books)
    return jsonify({'message': 'Book updated successfully'}), 200