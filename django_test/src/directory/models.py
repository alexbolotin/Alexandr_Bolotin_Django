from enum import unique
from re import T
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Genre name',
        max_length=20,
    )
    description= models.TextField(
        verbose_name='Genre description',
        blank =  True,
        null = True
    )

    def __str__(self) -> str:
        return str(self.id) + '. ' + self.name
    
class Book(models.Model):
    genre = models.ManyToManyField(
        'directory.Genre',
        verbose_name='Genre',
        related_name='genres'
    )
    publishing = models.ForeignKey(
        'directory.Publishing_house',
        on_delete=models.PROTECT,
        verbose_name='Publishing',
        related_name='publishing'
    )
    author = models.ManyToManyField(
        'directory.Author',
        # on_delete=models.PROTECT,
        verbose_name='Author',
        related_name='author'
    )
    name = models.CharField(
        verbose_name='Book name',
        max_length=30,
    )
    description= models.TextField(
        verbose_name='Book description',
        blank =  True,
        null = True
    )

    def __str__(self) -> str:
        return str(self.pk) + '. ' + self.name

class Publishing_house(models.Model):
    name = models.CharField(
        verbose_name='Publishing house',
        max_length=30,
    )
    description= models.TextField(
        verbose_name='Publishing house description',
        blank =  True,
        null = True
    )

    def __str__(self) -> str:
        return str(self.pk) + '. ' + self.name

class Author(models.Model):
    name = models.CharField(
        verbose_name='Author',
        max_length=30,
    )
    description= models.TextField(
        verbose_name='Author description',
        blank =  True,
        null = True
    )

    def __str__(self) -> str:
        return str(self.pk) + '. ' + self.name