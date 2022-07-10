# Generated by Django 4.0.5 on 2022-07-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_remove_book_author_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='directory.genre', verbose_name='Genre'),
        ),
    ]