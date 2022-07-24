from rest_framework import serializers

from read_book.models import Book, UserBookRelation


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__' # обработка всех позиций
        # fields = ['price'] # обработка только позиции price


class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'is_favorites', 'rate')
