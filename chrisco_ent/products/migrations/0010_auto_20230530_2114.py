# Generated by Django 3.2.15 on 2023-05-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20230530_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='new_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
            preserve_default=False,
        ),
    ]