from rest_framework import serializers

from read_book.models import Genres


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genres
        fields = ('genre',)
