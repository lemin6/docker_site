from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=16, unique=True)
    last_name = models.CharField(max_length=16, unique=True)
    birth_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=16, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    published_date = models.DateField()
    pages = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    have = models.BooleanField(default=True)

# DRF
# (CRUD)
# FILTER (author, published_date, have)
# SEARCH (title)
# EN RU ...
# PERMESS (iSoRrEAD)  + Github