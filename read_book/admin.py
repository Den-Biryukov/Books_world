from django.contrib import admin
from .models import Book, UserBookRelation, Comment, Genres, MyComments, Like, Rating

admin.site.register(Book)

admin.site.register(UserBookRelation)

admin.site.register(Comment)

admin.site.register(Genres)

admin.site.register(MyComments)

admin.site.register(Like)

admin.site.register(Rating)
