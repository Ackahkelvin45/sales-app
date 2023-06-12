# Generated by Django 3.2.15 on 2023-06-06 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0008_alter_sales_inventory'),
        ('debts', '0002_delete_sales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(blank=True, max_length=20, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('notes', models.TextField(blank=True, max_length=300, null=True)),
                ('paid_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('due_price', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recorder', to=settings.AUTH_USER_MODEL)),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sale_debt', to='sales.sales')),
            ],
        ),
    ]
