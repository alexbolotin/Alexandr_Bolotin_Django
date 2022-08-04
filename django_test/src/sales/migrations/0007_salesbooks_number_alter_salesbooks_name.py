# Generated by Django 4.0.5 on 2022-08-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_salesbooks_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesbooks',
            name='number',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Sales book number'),
        ),
        migrations.AlterField(
            model_name='salesbooks',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Sales book name'),
        ),
    ]