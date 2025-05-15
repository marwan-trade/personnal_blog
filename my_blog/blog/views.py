from django.shortcuts import render
from .models import Article, Category
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'blog/base.html')


def home(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def search(request):
    return HttpResponse("This is the search page.")