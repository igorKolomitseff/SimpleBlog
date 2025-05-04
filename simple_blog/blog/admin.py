from django.contrib import admin

from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published')
    list_filter = ('is_published',)
    actions = ('make_published',)

    @admin.action(description='Опубликовать выбранные статьи')
    def make_published(self, request, queryset):
        queryset.update(is_published=True)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
