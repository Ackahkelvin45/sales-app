# Generated by Django 3.2.15 on 2023-05-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.product'),
        ),
    ]
