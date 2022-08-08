from rest_framework import serializers
from read_book.models import Like, Book


class LikeFullNameOfBookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = serializers.CharField(default=Book)

    class Meta:
        model = Like
        fields = '__all__'
        # fields = ('like', 'book',)
        # exclude = ('user', )


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = '__all__'
        # fields = ('like', 'book',)
        # exclude = ('user', )
