from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, CreateTokenView,
                    GenreViewSet, RetrieveUpdateUserView, ReviewViewSet,
                    SignUpView, TitleViewSet, UserViewSet)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/users/me/',
         RetrieveUpdateUserView.as_view(),
         name='me'
         ),
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', CreateTokenView.as_view(), name='create_token'),
    path('v1/auth/signup/', SignUpView.as_view(), name='registration'),


]