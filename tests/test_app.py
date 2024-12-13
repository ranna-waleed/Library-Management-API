import unittest
from app import app

class TestLibraryAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/books', json={
            'title': 'Sample Book',
            'author': 'Author Name',
            'published_year': 2021,
            'isbn': '1234567890',
            'genre': 'Fiction'
        })
        self.assertEqual(response.status_code, 201)

    def test_list_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_search_books(self):
        response = self.app.get('/books/search?author=Author Name')
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete('/books/1234567890')
        self.assertEqual(response.status_code, 204)

    def test_update_book(self):
        response = self.app.put('/books/1234567890', json={'title': 'Updated Title'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()