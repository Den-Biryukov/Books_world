from django.db.models import Avg
from rest_framework import serializers
from read_book.models import Book, Like, Rating, MyComments
from read_book.serializer_comments import CommentSerializer
from read_book.serializer_genres import GenresSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # это поле для того, чтобы к примеру, когда мы обновляем или создаём запись,
    # т.е. чтобы в данный момент был только тот пользователь, который аутентифицирован и делает эти действия

    class Meta:
        model = Book
        fields = '__all__'


class BookWithFullOwnerSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)
    Comments = CommentSerializer(many=True)
    genres = GenresSerializer(many=True)

    likes_count = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    # is_favorites_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'author_name', 'price', 'owner', 'content', 'comments_count', 'Comments', 'genres',
                  'time_create', 'time_update', 'readers', 'likes_count', 'rating')

    def get_likes_count(self, instance):
        return Like.objects.filter(book=instance,
                                   like=True).count()

    def get_comments_count(self, instance):
        return MyComments.objects.filter(book=instance).count()

    def get_rating(self, instance):
        return Rating.objects.filter(book=instance).aggregate(Avg('rate'))

    #
    # def get_is_favorites_count(self, instance):
    #     return UserBookRelation.objects.filter(book=instance,
    #                                            is_favorites=True).count()
