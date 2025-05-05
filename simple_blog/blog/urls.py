from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'articles/<int:article_id>/',
        views.article_detail,
        name='article_detail'
    ),
    path(
        'articles/create/',
        views.article_create,
        name='article_create'
    ),
    path(
        'articles/<int:article_id>/edit/',
        views.article_edit,
        name='article_edit'
    ),
    path(
        'article/<int:article_id>/delete/',
        views.article_delete,
        name='article_delete'
    ),
]
