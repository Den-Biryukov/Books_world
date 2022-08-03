from django.contrib.auth.models import User
from rest_framework import generics

from read_book.pagination import ListPagination
from read_book.permissions import IsStaff
from read_book.serializer_User import UserSerializer


class AllUsersDetailListAPIView(generics.ListAPIView):
    """List information of users for staff"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsStaff, )
    pagination_class = ListPagination
