import unittest
from src.app import app

class LibraryManagementAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_year': 2021,
            'isbn': '1234567890',
            'genre': 'Fiction'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book added successfully', response.data)

    def test_list_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_search_books(self):
        response = self.app.get('/books/search', query_string={'author': 'Test Author'})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_delete_book(self):
        response = self.app.delete('/books/1234567890')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book deleted successfully', response.data)

    def test_update_book(self):
        response = self.app.put('/books/1234567890', json={
            'title': 'Updated Test Book',
            'author': 'Test Author',
            'published_year': 2021,
            'isbn': '1234567890',
            'genre': 'Non-Fiction'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Book updated successfully', response.data)

if __name__ == '__main__':
    unittest.main()