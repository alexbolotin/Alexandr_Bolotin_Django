# Generated by Django 4.0.5 on 2022-08-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.SmallIntegerField(default=1, verbose_name='Quantity'),
            preserve_default=False,
        ),
    ]