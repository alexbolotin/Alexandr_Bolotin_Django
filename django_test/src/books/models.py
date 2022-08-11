from statistics import quantiles
from django.db import models

# Create your models here.

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
        verbose_name='Author',
        related_name='author'
    )
    name = models.CharField(
        verbose_name='Book name',
        max_length=30,
    )

    series = models.CharField(
        verbose_name='Book series',
        max_length=30,
        blank =  True,
        null = True
    )

    description= models.TextField(
        verbose_name='Book description',
        blank =  True,
        null = True
    )

    picture = models.ImageField(
        verbose_name='Sales picture',
        upload_to = 'uploads/%Y/%m/%d/',
        blank =  True,
        null = True
    )

    quantity = models.SmallIntegerField(
        verbose_name= "Quantity",
    )

    price = models.DecimalField(
        verbose_name= "Price",
        decimal_places=2,
        max_digits=7,
        null = True,
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.pk) + '. ' + self.name