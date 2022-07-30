from rest_framework import serializers

from read_book.models import Book


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

    class Meta:
        model = Book
        fields = '__all__'
