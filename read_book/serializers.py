from rest_framework import serializers

from read_book.models import Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__' # обработка всех позиций
        # fields = ['price'] # обработка только позиции price
