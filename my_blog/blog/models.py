from django.db import models    # Import models to create database models
from django.utils.text import slugify   # Import slugify to create slugs from titles
from django.utils import timezone   # Import timezone to set the current time

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:   # Check if slug is not already set
            self.slug = slugify(self.name)  # Create a slug from the name
        super().save(*args, **kwargs)   # Call the parent save method

    def __str__(self):
        return self.name   # Return the name of the category when printed


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)    # Slug field for URL-friendly titles
    content = models.TextField()    # Content of the article
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')   # Foreign key to Category model
    published = models.BooleanField(default=False)   # Boolean field to mark if the article is published
    created_at = models.DateTimeField(default=timezone.now)   # DateTime field for creation time

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
