from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    """Book"""

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
    genres = models.ManyToManyField('Genres', blank=True)

    def __str__(self):
        return f'id - {self.id}: name - {self.name}'


class MyComments(models.Model):
    """Book comments"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Comment', max_length=3_000)
    book = models.ForeignKey(Book, verbose_name='books', on_delete=models.CASCADE, related_name='Comments')

    def __str__(self):
        return f'{self.id} - {self.owner} - {self.book}'

# старая модель
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

# старая модель комментариев
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False, related_name='comments')
    content = models.TextField()
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return f'some_comment -- {self.id}'


class Genres(models.Model):
    """Book genres"""

    GENRE_CHOICES = (
        ('mystery', 'Mystery'),
        ('thriller', 'Thriller'),
        ('horror', 'Horror'),
        ('historical', 'Historical'),
        ('romance', 'Romance'),
        ('western', 'Western'),
        ('bildungsroman', 'Bildungsroman'),
        ('speculative fiction', 'Speculative Fiction'),
        ('science fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('dystopian', 'Dystopian'),
        ('magical realism', 'Magical Realism'),
        ('realist literature', 'Realist Literature'),
        ('literary fiction', 'Literary Fiction'),
    )

    genre = models.CharField(choices=GENRE_CHOICES, blank=True,
                             max_length=50, unique=True)

    def __str__(self):
        return f'id - {self.id}: {self.genre}'


class Like(models.Model):
    """Book likes"""

    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('like', 'user', 'book')

    def __str__(self):
        return f'user: {self.user}; book: {self.book}; like: {self.like}'


class Rating(models.Model):
    """Book rating"""

    RATE_CHOICES = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'OK'),
        (4, 'COOL'),
        (5, 'AMAZING')
    )

    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')
