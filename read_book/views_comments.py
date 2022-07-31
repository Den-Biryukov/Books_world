from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import MyComments
from .permissions import IsOwnerOrStaffOrReadOnly, IsOwnerOrReadOnly
from .serializer_Comments import CommentCreateDeleteSerializer, CommentWithFullOwnerAndBookSerializer, \
    CommentUpdateSerializer
from rest_framework.response import Response


class CommentCreateView(APIView):
    """Create comment"""

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        comment = CommentCreateDeleteSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


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
