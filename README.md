# Library Management API

## Description
A RESTful API for managing a collection of books in a library.

### Prerequisites
- Python 3.9 
- Docker

### Installation

1. **Clone the repository:**
   ```bash
   git clone (https://github.com/ranna-waleed/Library-Management-API)
   cd library-management-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the API

1. **Start the Flask application:**
   ```bash
   python src/app.py
   ```

2. **Access the API:**
   Open your browser and go to `http://127.0.0.1:5000`.

### API Endpoints

- `POST /books`: Add a new book
- `GET /books`: List all books
- `GET /books/search`: Search for books
- `DELETE /books/:isbn`: Delete book by ISBN
- `PUT /books/:isbn`: Update book details by ISBN

### Running Tests

1. **Using `unittest`:**
   ```bash
   python -m unittest discover -s tests
   ```

### Docker

1. **Build the Docker image:**
   ```bash
   docker build -t library-management-api .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 library-management-api
   ```

3. **Access the API:**
   Open your browser and go to `http://127.0.0.1:5000`.

### Postman Collection

A Postman collection containing requests for all API functionalities is included in the repository under `static/postman_collection.json`file.

### Swagger Documentation

The Swagger documentation for the API is available in the `static/swagger.json` file.


