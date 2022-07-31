from rest_framework import serializers
from read_book.models import MyComments


class CommentCreateDeleteSerializer(serializers.ModelSerializer):
    """Create and delete comment"""

    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyComments
        fields = "__all__"


class CommentUpdateSerializer(serializers.ModelSerializer):
    """Update comment"""

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyComments
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """List comments on mane page"""

    owner = serializers.CharField(read_only=True)

    class Meta:
        model = MyComments
        fields = ('owner', 'text')


class CommentWithFullOwnerAndBookSerializer(serializers.ModelSerializer):
    """Instead of id book and owner show their name"""

    owner = serializers.CharField(read_only=True)
    book = serializers.CharField(read_only=True)

    class Meta:
        model = MyComments
        fields = '__all__'
