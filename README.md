# Library Management API

## Project Overview
This project is a RESTful API for managing a collection of books in a library. Data is stored in a JSON file.


## Features

- Add a new book with details such as title, author, published year, ISBN, and genre.
- List all books in the library.
- Search for books by author, published year, or genre.
- Delete book by its ISBN.
- Update book details by its ISBN.

## Prerequisites
- Python 3.x
- Docker (optional)
- Git

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ranna-waleed/Library-Management-API.git
   cd Library-Management-API

2. Create and Activate Virtual Environment

      python -m venv venv
      source venv/bin/activate  # On macOS/Linux
      .\venv\Scripts\activate  # On Windows

## Docker Integration
Build the Docker Image: docker build -t library-management-api .

Run the Docker Container: docker run -p 5000:5000 library-management-api

## Running the Application
 flask run