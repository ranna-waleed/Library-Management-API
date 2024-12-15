import sys
import os
from flask import Flask

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.routes.book_routes import book_bp

app = Flask(__name__)
app.register_blueprint(book_bp)

@app.route('/')
def home():
    return "Welcome to the Library Management API!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)