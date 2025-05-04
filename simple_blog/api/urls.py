from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, TagViewSet


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('tags', TagViewSet, basename='tag')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
