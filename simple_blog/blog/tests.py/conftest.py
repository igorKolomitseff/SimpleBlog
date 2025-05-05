import pytest
from django.test.client import Client
from django.urls import reverse

from blog.models import Article, Tag


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Author')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def tag1():
    return Tag.objects.create(name='Django')


@pytest.fixture
def tag2():
    return Tag.objects.create(name='Python')


@pytest.fixture
def article_data(tag1, tag2):
    return {
        'title': 'Test Article',
        'content': 'Test article content.',
        'is_published': True,
        'tags': [tag1.pk, tag2.pk]
    }


@pytest.fixture
def article(author, tag1, tag2):
    article = Article.objects.create(
        title='Test Article',
        content='Test article content.',
        author=author,
        is_published=True,
    )
    article.tags.set([tag1, tag2])
    return article


@pytest.fixture
def a_lot_of_articles(author, tag1, tag2):
    articles = []
    for index in range(10):
        article = Article.objects.create(
            title=f'Test Article {index}',
            content='Test article content.',
            author=author,
            is_published=index % 2 == 0
        )
        article.tags.set([tag1, tag2])
        articles.append(article)
    return articles


@pytest.fixture
def login_url():
    return '/auth/login/'


@pytest.fixture
def article_create_url():
    return reverse('blog:article_create')


@pytest.fixture
def article_edit_url(article):
    return reverse('blog:article_edit', args=(article.id,))
