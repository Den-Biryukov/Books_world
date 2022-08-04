from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from read_book.models import Book
from rest_framework import status
from read_book.serializer_Book import BookWithFullOwnerSerializer, BookCreateUpdateSerializer
import json


class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test_user@mail.ru', username='test_user',
                                        password='test_password123')
        self.user_2 = User.objects.create(email='test_user_2@mail.ru', username='test_user_2',
                                          password='test_2_password123')
        self.user_3_staff = User.objects.create(email='test_user_3@mail.ru', username='test_user_3',
                                                password='test_3_password123', is_staff=True)

        self.book_1 = Book.objects.create(name='Test_book_1', content='some content', price=10,
                                          author_name='Author_1', owner=self.user)
        self.book_2 = Book.objects.create(name='Test_book_2', content='some content', price=20,
                                          author_name='Author_2', owner=self.user)

    def test_get(self):
        url = 'http://127.0.0.1:8000/api/v1/book/'
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_search(self):
        url = 'http://127.0.0.1:8000/api/v1/book/'
        response = self.client.get(url, data={'search': 'Author 1'})
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create(self):
        self.assertEqual(2, Book.objects.all().count())
        url = 'http://127.0.0.1:8000/api/v1/book/'
        data = {
            "name": "Programming in Python 3",
            "content": "python",
            "price": 1,
            "author_name": "Mark Summerfield"
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Book.objects.all().count())
        self.assertEqual(self.user, Book.objects.last().owner)

    def test_create_not_authenticated(self):
        self.assertEqual(2, Book.objects.all().count())
        url = 'http://127.0.0.1:8000/api/v1/book/'
        data = {
            "name": "Programming in Python 3 (new)",
            "content": "python",
            "price": 1,
            "author_name": "Mark Summerfield"
        }
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
        self.assertEqual(2, Book.objects.all().count())

    def test_delete(self):
        self.assertEqual(2, Book.objects.all().count())
        url = 'http://127.0.0.1:8000/api/v1/book/delete/1'
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, Book.objects.all().count())

    def test_delete_not_owner(self):
        url = 'http://127.0.0.1:8000/api/v1/book/delete/1'
        self.client.force_login(self.user_2)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_delete_not_owner_but_staff(self):
        url = 'http://127.0.0.1:8000/api/v1/book/delete/1'
        self.client.force_login(self.user_3_staff)
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_update(self):
        url = 'http://127.0.0.1:8000/api/v1/book/update/1'
        data = {
            "name": self.book_1.name,
            "content": self.book_1.content,
            "price": 15,
            "author_name": self.book_1.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(15, self.book_1.price)

    def test_update_not_owner(self):
        url = 'http://127.0.0.1:8000/api/v1/book/update/1'
        data = {
            "name": self.book_1.name,
            "content": self.book_1.content,
            "price": 15,
            "author_name": self.book_1.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user_2)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.book_1.refresh_from_db()
        self.assertEqual(10, self.book_1.price)
