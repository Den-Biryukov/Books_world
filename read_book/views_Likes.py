from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from read_book.permissions import UserIsOwnerOrReadOnly
from read_book.serializer_Likes import LikeSerializer
from read_book.models import Like


class LikeCreateAPIView(generics.ListCreateAPIView):
    """Create like"""

    permission_classes = (IsAuthenticated, )
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeDeleteAPIView(mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin, GenericAPIView):
    """Delete like"""

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    permission_classes = (UserIsOwnerOrReadOnly,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
