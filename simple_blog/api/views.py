from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import Article, Tag
from .pagination import BasePagination
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    ArticleSerializer,
    ArticleWriteSerializer,
    TagSerializer
)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.select_related(
            'author'
        ).prefetch_related(
            'tags'
        )
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_published',)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ArticleWriteSerializer
        return ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
