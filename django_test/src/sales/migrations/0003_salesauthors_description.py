# Generated by Django 4.0.5 on 2022-07-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_salesauthors_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesauthors',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Sales description'),
        ),
    ]
