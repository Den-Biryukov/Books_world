from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from read_book.permissions import UserIsOwnerOrReadOnly
from read_book.serializer_Rating import RatingFullNameOfBookSerializer, RatingSerializer
from read_book.models import Rating


class RatingCreateAPIView(generics.ListCreateAPIView):
    """Create Rating"""

    permission_classes = (IsAuthenticated, )
    # serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RatingFullNameOfBookSerializer
        else:
            return RatingSerializer


class RatingDeleteAPIView(mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin, GenericAPIView):
    """Delete Rating"""

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    permission_classes = (UserIsOwnerOrReadOnly, )
    serializer_class = RatingFullNameOfBookSerializer
    queryset = Rating.objects.all()
