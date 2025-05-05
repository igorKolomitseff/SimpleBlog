from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.filter(
        is_published=True
    ).select_related(
        'author'
    ).prefetch_related('tags')
    paginator = Paginator(articles, settings.PAGE_SIZE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})


@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('blog:article_detail', article_id=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/create.html', {'form': form})


@login_required
def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:article_detail', article_id=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/create.html', {'form': form})


@login_required
def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if article.author != request.user:
        return redirect('blog:article_detail', article_id=article_id)
    article.delete()
    return redirect('blog:index')
