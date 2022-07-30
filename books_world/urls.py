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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from read_book.views_BookViewSet import BookViewSet, auth_login_github
from read_book.views_UserBooksRelationView import UserBooksRelationView

router = SimpleRouter()

router.register(r'books', BookViewSet)
router.register(r'books_relation', UserBooksRelationView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('read_book.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth_log_github/', auth_login_github),

    # djoser
    path('api/v1/auth_djoser/', include('djoser.urls')),
    re_path(r'^auth_djoser/', include('djoser.urls.authtoken')),

    # urls for JWT auth
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
