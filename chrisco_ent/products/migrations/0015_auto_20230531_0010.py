# Generated by Django 3.2.15 on 2023-05-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20230531_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='new_total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
