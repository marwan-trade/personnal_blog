from django.shortcuts import render
from .models import Article, Category

# Create your views here.


def home(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})
