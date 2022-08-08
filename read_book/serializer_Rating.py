from rest_framework import serializers
from read_book.models import Rating, Book


class RatingFullNameOfBookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = serializers.CharField(default=Book)

    class Meta:
        model = Rating
        exclude = ('id',)


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        exclude = ('id',)
