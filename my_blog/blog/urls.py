from django.urls import path
from . import views

app_name = 'blog'  # This is the namespace for the app, used in templates and URL reversing
urlpatterns = [
    path('', views.home, name='home'),
    path("base/", views.base, name="base"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"), # Assuming you have a search view
]
