import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from read_book.models import Book, UserBookRelation


class BooksRelationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_username', )
        self.user2 = User.objects.create(username='test_username2', )
        self.book_1 = Book.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1',
                                          owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2', price=50,
                                          author_name='Author 2')

    def test_like(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id,))

        data = {
            "like": True,
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data,
                                     content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserBookRelation.objects.get(user=self.user,
                                                book=self.book_1)
        self.assertTrue(relation.like)
