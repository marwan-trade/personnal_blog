from django.shortcuts import render
from .models import Article, Category
from django.http import HttpResponse

# Create your views here.

def base(request):
    return render(request, 'blog/base.html')


def home(request):
    return HttpResponse("This is the home page.")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def search(request):
    return HttpResponse("This is the search page.")