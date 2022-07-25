from rest_framework import serializers

from read_book.models import Book, UserBookRelation


class BooksSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        # fields = '__all__' # обработка всех позиций
        # fields = ['price'] # обработка только позиции price
        fields = ('id', 'name', 'price', 'author_name', 'likes_count')

    def get_likes_count(self, instance):
        return UserBookRelation.objects.filter(book=instance,
                                               like=True).count()


class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'is_favorites', 'rate')
