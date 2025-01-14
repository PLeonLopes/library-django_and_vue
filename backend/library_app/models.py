from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)         # isbn tem 13 caracteres e é único
    pages = models.IntegerField()
    cover = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title