from django.contrib.auth.models import User
from django.test import TestCase
from read_book.models import Book, UserBookRelation
from read_book.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        book_1 = Book.objects.create(name='Test book 1', price=25,
                                     author_name='Author 1', content='')
        book_2 = Book.objects.create(name='Test book 2', price=50,
                                     author_name='Author 2', content='')

        # Test likes_count for book_1 and book_2
        UserBookRelation.objects.create(user=user1, book=book_1, like=True)
        UserBookRelation.objects.create(user=user2, book=book_1, like=True)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True)

        UserBookRelation.objects.create(user=user1, book=book_2, like=False)
        UserBookRelation.objects.create(user=user2, book=book_2, like=True)
        UserBookRelation.objects.create(user=user3, book=book_2, like=False)

        # Test is_favorites_count for book_1 and book_2
        UserBookRelation.objects.create(user=user1, book=book_1, is_favorites=True)
        UserBookRelation.objects.create(user=user2, book=book_1, is_favorites=True)
        UserBookRelation.objects.create(user=user3, book=book_1, is_favorites=True)

        UserBookRelation.objects.create(user=user1, book=book_2, is_favorites=True)
        UserBookRelation.objects.create(user=user2, book=book_2, is_favorites=True)
        UserBookRelation.objects.create(user=user3, book=book_2, is_favorites=False)

        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.00',
                'author_name': 'Author 1',
                'likes_count': 3,
                'is_favorites_count': 3,
                'content': ''
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '50.00',
                'author_name': 'Author 2',
                'likes_count': 1,
                'is_favorites_count': 2,
                'content': ''
            },
        ]
        self.assertEqual(expected_data, data)
