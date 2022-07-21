from django.test import TestCase
from read_book.models import Book
from read_book.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=25,
                                     author_name='Author 1')
        book_2 = Book.objects.create(name='Test book 2', price=50,
                                     author_name='Author 2')
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1'
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '50.00',
                'author_name': 'Author 2'
            },
        ]
        self.assertEqual(expected_data, data)