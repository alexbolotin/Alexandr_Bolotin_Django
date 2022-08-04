from distutils.command.upload import upload
from django.db import models
from directory import models as dirs
from books import models as books

# Create your models here.
class SalesBooks(models.Model):
    name = models.TextField(
        verbose_name='Sales book name',
        blank =  True,
        null = True
    )

    number = models.BigIntegerField(
        verbose_name='Sales book number',
        blank =  True,
        null = True
    )
    
    picture = models.ImageField(
        verbose_name='Sales picture',
        upload_to = 'uploads/%Y/%m/%d/',
        blank =  True,
        null = True
    )
    book = models.ManyToManyField(
        'books.Book',
        verbose_name='Sale_book',
        related_name='sale_book',
    )
    
    description= models.TextField(
        verbose_name='Sales book description',
        blank =  True,
        null = True
    )
    def __str__(self) -> str:
        return self.name

class SalesAuthors(models.Model):
    name = models.TextField(
        verbose_name='Sales author number',
        blank =  True,
        null = True
    )

    number = models.BigIntegerField(
        verbose_name='Sales author number',
        blank =  True,
        null = True
    )

    picture = models.ImageField(
        verbose_name='Sales picture',
        upload_to = 'uploads/%Y/%m/%d/',
        blank =  True,
        null = True
    )

    authors = models.ManyToManyField(
        'directory.Author',
        verbose_name='top_author',
        related_name='top_author',
    )
    description= models.TextField(
        verbose_name='Sales author description',
        blank =  True,
        null = True
    )

    def __str__(self) -> str:
        return str(self.name)