# Generated by Django 4.0.5 on 2022-08-09 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_series'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Price')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='books.book', verbose_name='Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='orders.cart', verbose_name='Cart')),
            ],
        ),
    ]