from django.urls import path
from read_book.views_Book import BookAPIView, BookRetrieveUpdateDestroyAPIView, BookListCreateAPIView, \
    BookListdetailUpdateAPIView, BookListdetailDeleteAPIVew

# Book
urlpatterns = [
    # path('book/', BookAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('book/update/<int:pk>', BookListdetailUpdateAPIView.as_view()),
    path('book/delete/<int:pk>', BookListdetailDeleteAPIVew.as_view()),
    # path('book/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
]
