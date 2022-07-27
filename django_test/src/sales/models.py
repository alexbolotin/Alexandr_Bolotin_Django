from django.db import models
from directory import models as dirs

# Create your models here.
class SalesBooks(models.Model):
    book = models.ManyToManyField(
        'directory.Book',
        verbose_name='Sale_book',
        related_name='sale_book',
    )
    name = models.TextField(
        verbose_name='Sales book number',
        blank =  True,
        null = True
    )
    description= models.TextField(
        verbose_name='Sales book description',
        blank =  True,
        null = True
    )
    def __str__(self) -> str:
        return self.description

class SalesAuthors(models.Model):
    name = models.TextField(
        verbose_name='Sales author number',
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
        return str(self.description)