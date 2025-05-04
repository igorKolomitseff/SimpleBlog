from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=settings.TAG_NAME_MAX_LENGTH,
        unique=True,
        verbose_name='Название тега'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        max_length=settings.ARTICLE_TITLE_MAX_LENGTH,
        verbose_name='Заголовок статьи'
    )
    content = models.TextField(
        verbose_name='Текст статьи'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор статьи'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано'
    )
    tags = models.ManyToManyField(
        Tag,
        through='ArticleTag',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ('-created_at',)
        default_related_name = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return (
            f'"{self.title}". {self.content[:settings.TEXT_MAX_LENGTH]} ... | '
            f'{self.created_at.strftime("%d.%m.%Y %H:%M")} | '
            f'От автора {self.author}'
        )


class ArticleTag(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name='Статья'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        ordering = ('article', 'tag')
        verbose_name = 'Статья - тег'
        verbose_name_plural = 'статьи - теги'

    def __str__(self):
        return f'{self.article.title} - {self.tag.name}'
