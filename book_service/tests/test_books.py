import unittest
from app import app

class BookServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_books_endpoint(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), ["1984", "Dune", "Harry Potter"])

if __name__ == '__main__':
    unittest.main()
