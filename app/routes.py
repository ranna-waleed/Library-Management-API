from flask import request, jsonify
from app import app
from app.models import Book, load_books, save_books

@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        books = load_books()
        books.append(new_book)
        save_books(books)
        return jsonify(new_book.to_dict()), 201
    except Exception as e:
        return str(e), 500

@app.route('/books', methods=['GET'])
def list_books():
    try:
        books = load_books()
        return jsonify([book.to_dict() for book in books]), 200
    except Exception as e:
        return str(e), 500

@app.route('/books/search', methods=['GET'])
def search_books():
    try:
        author = request.args.get('author')
        published_year = request.args.get('published_year')
        genre = request.args.get('genre')
        books = load_books()
        filtered_books = [book for book in books if
                          (author is None or book.author == author) and
                          (published_year is None or book.published_year == int(published_year)) and
                          (genre is None or book.genre == genre)]
        return jsonify([book.to_dict() for book in filtered_books]), 200
    except Exception as e:
        return str(e), 500

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    try:
        books = load_books()
        books = [book for book in books if book.isbn != isbn]
        save_books(books)
        return '', 204
    except Exception as e:
        return str(e), 500

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    try:
        data = request.get_json()
        books = load_books()
        for book in books:
            if book.isbn == isbn:
                book.title = data.get('title', book.title)
                book.author = data.get('author', book.author)
                book.published_year = data.get('published_year', book.published_year)
                book.genre = data.get('genre', book.genre)
                save_books(books)
                return jsonify(book.to_dict()), 200
        return '', 404
    except Exception as e:
        return str(e), 500