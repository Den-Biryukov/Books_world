from rest_framework import generics, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from read_book.models import Book
from read_book.pagnation import ListPagination
from read_book.permissions import IsOwnerOrReadOnly, IsOwnerOrStaffOrReadOnly
from read_book.serializer_Book import BookSerializer, BookCreateUpdateSerializer, BookWithFullOwnerSerializer


class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookWithFullOwnerSerializer
        else:
            return BookCreateUpdateSerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = ListPagination
    queryset = Book.objects.all()



class BookListdetailUpdateAPIView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin, GenericAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookWithFullOwnerSerializer
        else:
            return BookCreateUpdateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Book.objects.all()



class BookListdetailDeleteAPIVew(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    permission_classes = (IsOwnerOrStaffOrReadOnly, )
    queryset = Book.objects.all()
    serializer_class = BookWithFullOwnerSerializer
