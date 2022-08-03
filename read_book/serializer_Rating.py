from rest_framework import serializers
from read_book.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        exclude = ('id',)
