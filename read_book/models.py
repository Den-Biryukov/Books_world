from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True)

    def __str__(self):
        return f'id - {self.id}: name - {self.name}'


class UserBookRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'OK'),
        (4, 'COOL'),
        (5, 'AMAZING')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    is_favorites = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
