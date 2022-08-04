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


class Series(models.Model):
    name = models.CharField(
        verbose_name='Series',
        max_length=30,
    )
    description= models.TextField(
        verbose_name='Series description',
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


