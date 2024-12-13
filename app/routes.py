from flask import Blueprint, request, jsonify
from .models import Book, read_books, write_books

main = Blueprint('main', __name__)

@main.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books = read_books()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_year=data['published_year'],
        isbn=data['isbn'],
        genre=data.get('genre')
    )
    books.append(new_book.to_dict())
    write_books(books)
    return jsonify({'message': 'Book added successfully!'}), 201

@main.route('/books', methods=['GET'])
def get_books():
    books = read_books()
    return jsonify({'books': books})

@main.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()
    books = read_books()
    book = next((b for b in books if b['isbn'] == isbn), None)
    if not book:
        return jsonify({'message': 'Book not found!'}), 404

    book.update({
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author']),
        'published_year': data.get('published_year', book['published_year']),
        'genre': data.get('genre', book.get('genre'))
    })
    write_books(books)
    return jsonify({'message': 'Book updated successfully!'})

@main.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    books = read_books()
    book = next((b for b in books if b['isbn'] == isbn), None)
    if not book:
        return jsonify({'message': 'Book not found!'}), 404

    books.remove(book)
    write_books(books)
    return jsonify({'message': 'Book deleted successfully!'})