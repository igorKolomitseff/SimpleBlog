from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, TagViewSet


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('tags', TagViewSet, basename='tag')


urlpatterns = [
    path(
        'auth/register/',
        UserViewSet.as_view({'post': 'create'}),
        name='user-create'
    ),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]

urlpatterns += [
    path(
        'schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
