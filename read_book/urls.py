from django.urls import path
from read_book.views_Book import BookAPIView, BookRetrieveUpdateDestroyAPIView, BookListCreateAPIView, \
    BookListdetailUpdateAPIView, BookListdetailDeleteAPIVew
from read_book.views_Comments import CommentListCreateView, CommentDeleteAPIView, CommentUpdateAPIView
from read_book.views_Likes import LikeCreateAPIView, LikeDeleteAPIView
from read_book.views_Rating import RatingCreateAPIView, RatingDeleteAPIView
from read_book.views_User import AllUsersForStaffListAPIView, UserDetailLikesAPIView, UserListAPIView, \
    UserDetailForStaffListAPIView, UserDetailListAPIView, UserDetailRatingAPIView


# Book
urlpatterns = [
    # path('book/', BookAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('book/update/<int:pk>', BookListdetailUpdateAPIView.as_view()),
    path('book/delete/<int:pk>', BookListdetailDeleteAPIVew.as_view()),
    # path('book/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
]

# Comment
urlpatterns += [
    path('comments/', CommentListCreateView.as_view()),
    path('comment_delete/<int:pk>', CommentDeleteAPIView.as_view()),
    path('comment_update/<int:pk>', CommentUpdateAPIView.as_view()),
]

# Like
urlpatterns += [
    path('like_create/', LikeCreateAPIView.as_view()),
    path('like_delete/<int:pk>', LikeDeleteAPIView.as_view()),
    path('user/<int:pk>/likes', UserDetailLikesAPIView.as_view()),
]

# Rating
urlpatterns += [
    path('rating_create/', RatingCreateAPIView.as_view()),
    path('rating_delete/<int:pk>', RatingDeleteAPIView.as_view())
]

# User
urlpatterns += [
    path('all_users_staff/', AllUsersForStaffListAPIView.as_view()),
    path('all_users/', UserListAPIView.as_view()),
    path('user_staff/<int:pk>', UserDetailForStaffListAPIView.as_view()),
    path('user/<int:pk>', UserDetailListAPIView.as_view()),
    path('user/<int:pk>/likes', UserDetailLikesAPIView.as_view()),
    path('user/<int:pk>/rating', UserDetailRatingAPIView.as_view()),
]
