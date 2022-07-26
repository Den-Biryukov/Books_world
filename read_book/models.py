from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              null=True, related_name='my_books',
                              verbose_name='book_owner')
    readers = models.ManyToManyField(User, through='UserBookRelation',
                                     related_name='books')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

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
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}: {self.book.name}, rating is {self.rate}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    content = models.TextField()
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f'some_comment -- {self.id}'


class Genres(models.Model):
    GENRE_CHOICES = (
        (1, 'Mystery'),
        (2, 'Thriller'),
        (3, 'Horror'),
        (4, 'Historical'),
        (5, 'Romance'),
        (6, 'Western'),
        (7, 'Bildungsroman'),
        (8, 'Speculative Fiction'),
        (9, 'Science Fiction'),
        (10, 'Fantasy'),
        (11, 'Dystopian'),
        (12, 'Magical Realism'),
        (13, 'Realist Literature'),
        (14, 'Literary Fiction'),
    )
    genre = models.PositiveSmallIntegerField(choices=GENRE_CHOICES,
                                             blank=True, null=True)
    book = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return f'{self.genre}'

