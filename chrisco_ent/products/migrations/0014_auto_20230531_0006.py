# Generated by Django 3.2.15 on 2023-05-31 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20230530_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='new_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='new_total_price',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=100, null=True), max_digits=100),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=100, null=True),
        ),
    ]
