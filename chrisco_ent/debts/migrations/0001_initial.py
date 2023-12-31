# Generated by Django 3.2.15 on 2023-05-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_alter_productitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('total_quantity', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=300, null=True)),
                ('paid_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('due_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('products', models.ManyToManyField(blank=True, related_name='products_sales', to='products.ProductItem')),
            ],
        ),
    ]
