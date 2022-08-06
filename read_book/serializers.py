from rest_framework import serializers

from read_book.models import Book, UserBookRelation

# старый сериализатор
class BooksSerializer(serializers.ModelSerializer):

    likes_count = serializers.SerializerMethodField()
    is_favorites_count = serializers.SerializerMethodField()


    class Meta:
        model = Book
        # fields = '__all__' # обработка всех позиций
        # fields = ['price'] # обработка только позиции price
        fields = ('id', 'name', 'price', 'author_name', 'likes_count',
                  'is_favorites_count', 'owner', 'readers', 'content', 'genres')

    def get_likes_count(self, instance):
        return UserBookRelation.objects.filter(book=instance,
                                               like=True).count()

    def get_is_favorites_count(self, instance):
        return UserBookRelation.objects.filter(book=instance,
                                               is_favorites=True).count()

class UserBookRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'is_favorites', 'rate')

