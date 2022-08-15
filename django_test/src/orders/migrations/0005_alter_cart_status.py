# Generated by Django 4.0.5 on 2022-08-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('Start', 'Start'), ('Request', 'Request'), ('Processing', 'Processing'), ('Paid', 'Paid'), ('Delivery', 'Delivery'), ('Problemm', 'Problemm'), ('Cancel', 'Cancel'), ('Close', 'Close')], default='Start', max_length=15),
        ),
    ]