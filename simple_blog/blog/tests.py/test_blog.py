import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from blog.forms import ArticleForm
from blog.models import Article

pytestmark = pytest.mark.django_db


def test_user_can_create_article(
    author_client, author, article_data, article_create_url, tag1, tag2
):
    response = author_client.post(
        article_create_url,
        data=article_data
    )
    article = Article.objects.first()
    assertRedirects(
        response,
        reverse('blog:article_detail', args=(article.id,))
    )
    assert Article.objects.count() == 1
    assert article.title == article_data['title']
    assert article.content == article_data['content']
    assert article.author == author
    assert set(article.tags.all()) == {tag1, tag2}


def test_anonymous_user_cant_create_article(
    client, article_data, article_create_url, login_url
):
    response = client.post(
        article_create_url,
        data=article_data
    )
    assertRedirects(
        response,
        f'{login_url}?next={article_create_url}'
    )
    assert Article.objects.count() == 0


def test_published_articles_filter(a_lot_of_articles):
    published = Article.objects.filter(is_published=True)
    assert published.count() == 5
    for article in published:
        assert article.is_published


def test_author_client_has_form(author_client, article_edit_url):
    response = author_client.get(article_edit_url)
    assert response.status_code == 200
    assert isinstance(response.context.get('form'), ArticleForm)


def test_anonymous_client_has_no_form(client, article_edit_url, login_url):
    assertRedirects(
        client.get(article_edit_url),
        f'{login_url}?next={article_edit_url}'
    )
