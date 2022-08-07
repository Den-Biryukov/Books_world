from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MyComments
from .pagination import ListPagination
from .permissions import IsOwnerOrStaffOrReadOnly, IsOwnerOrReadOnly
from .serializer_comments import CommentCreateDeleteSerializer, CommentWithFullOwnerAndBookSerializer, \
                                 CommentUpdateSerializer
from .tasks import clear_comments



class CommentListCreateView(generics.ListAPIView, generics.ListCreateAPIView):
    """Create comment"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentWithFullOwnerAndBookSerializer
        else:
            return CommentCreateDeleteSerializer

    def post(self, request, *args, **kwargs):
        clear_comments.delay()
        return self.create(request, *args, **kwargs)

    queryset = MyComments.objects.all()
    pagination_class = ListPagination
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentDeleteAPIView(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin, GenericAPIView):
    """Delete comment"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentWithFullOwnerAndBookSerializer
        else:
            return CommentCreateDeleteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    permission_classes = (IsOwnerOrStaffOrReadOnly, )
    queryset = MyComments.objects.all()


class CommentUpdateAPIView(mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin, GenericAPIView):
    """Update comment"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentWithFullOwnerAndBookSerializer
        else:
            return CommentUpdateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    permission_classes = (IsOwnerOrReadOnly, )
    queryset = MyComments.objects.all()
    serializer_class = CommentCreateDeleteSerializer
