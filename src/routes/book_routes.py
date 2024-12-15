from flask import Blueprint
from src.controllers import book_controller

book_bp = Blueprint('book_bp', __name__)

book_bp.route('/books', methods=['POST'])(book_controller.add_book)
book_bp.route('/books', methods=['GET'])(book_controller.list_books)
book_bp.route('/books/search', methods=['GET'])(book_controller.search_books)
book_bp.route('/books/<string:isbn>', methods=['DELETE'])(book_controller.delete_book)
book_bp.route('/books/<string:isbn>', methods=['PUT'])(book_controller.update_book)