"""books_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from read_book.views_Book import BookAPIView, BookCreateAPIView, \
                                 BookRetrieveUpdateDestroyAPIView
from read_book.views_BookViewSet import BookViewSet, auth
from read_book.views_UserBooksRelationView import UserBooksRelationView

router = SimpleRouter()

router.register(r'books', BookViewSet)
router.register(r'books_relation', UserBooksRelationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book/', BookAPIView.as_view()),
    path('api/v1/book/create/', BookCreateAPIView.as_view()),
    path('api/v1/book/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth)
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
