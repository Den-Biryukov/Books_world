from rest_framework import serializers
from read_book.models import Like, Book


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = serializers.CharField(default=Book)

    class Meta:
        model = Like
        fields = ('user', 'book',)
