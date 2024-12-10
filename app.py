from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, doc='/api-docs')

books = []

book_model = api.model('Book', {
    'title': fields.String(required=True, description='The book title'),
    'author': fields.String(required=True, description='The book author'),
    'publishedYear': fields.Integer(required=True, description='The year the book was published'),
    'isbn': fields.String(required=True, description='The book ISBN'),
    'genre': fields.String(description='The book genre')
})

@api.route('/books')
class BookList(Resource):
    @api.doc('list_books')
    def get(self):
        return books

    @api.expect(book_model)
    @api.doc('add_book')
    def post(self):
        new_book = api.payload
        books.append(new_book)
        return new_book, 201

@api.route('/books/<string:isbn>')
@api.doc(params={'isbn': 'The book ISBN'})
class Book(Resource):
    def delete(self, isbn):
        global books
        books = [book for book in books if book['isbn'] != isbn]
        return '', 204

    @api.expect(book_model)
    def put(self, isbn):
        updated_details = api.payload
        for book in books:
            if book['isbn'] == isbn:
                book.update(updated_details)
                return book
        return {'message': 'Book not found'}, 404

@api.route('/books/search')
class BookSearch(Resource):
    def get(self):
        author = request.args.get('author')
        published_year = request.args.get('publishedYear')
        genre = request.args.get('genre')
        filtered_books = books

        if author:
            filtered_books = [book for book in filtered_books if book['author'] == author]
        if published_year:
            filtered_books = [book for book in filtered_books if book['publishedYear'] == int(published_year)]
        if genre:
            filtered_books = [book for book in filtered_books if book['genre'] == genre]

        return filtered_books

if __name__ == '__main__':
    app.run(debug=True)