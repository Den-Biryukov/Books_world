import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from read_book.models import Book
from read_book.serializers import BooksSerializer


class BooksAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_username', )
        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=50,
                                          author_name='Author 2')
        self.book_3 = Book.objects.create(name='Test book Author 1', price=8,
                                          author_name='Author 3')

    def test_get(self):
        url = 'http://127.0.0.1:8000/books/'
        response = self.client.get(url)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3],
                                          many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data, '- это ответ на запрос, который мы сейчас отправили')

    def test_get_search(self):
        url = 'http://127.0.0.1:8000/books/'
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerializer([self.book_1, self.book_3],
                                          many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(response.data, '- это ответ на запрос, который мы сейчас отправили')

    def test_create(self):
        self.assertEqual(3, Book.objects.all().count())
        url = 'http://127.0.0.1:8000/books/'
        data = {
            "name": "Programming in Python 3",
            "price": 99,
            "author_name": "Mark Summerfield"
        }
        json_data = json.dumps(data)
        print(json_data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Book.objects.all().count())

    def test_update(self):
        url = reverse('book-detail', args=(self.book_1.id,))
        data = {
            "name": self.book_1.name,
            "price": 57,
            "author_name": self.book_1.author_name
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(url, data=json_data,
                                   content_type='application/json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)