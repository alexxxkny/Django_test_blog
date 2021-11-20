from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
header_menu = [
    {'title': 'Главная', 'url_name': 'blog:home'},
    {'title': 'Статьи', 'url_name': 'blog:articles'},
    {'title': 'Добавить статью', 'url_name': 'blog:add_article'},
    {'title': 'О нас', 'url_name': 'blog:about'}
]


def index(request):
    return render(request, 'blog/home.html')


def articles(request):
    return render(request, 'blog/articles.html')


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'blog/article.html', context)


def login(request):
    return render(request, 'blog/login.html')


def add_article(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            try:
                Article.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, 'Ошибка')
            else:
                return redirect('blog:articles')
    else:
        form = AddArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html')