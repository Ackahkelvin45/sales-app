# Generated by Django 3.2.15 on 2023-05-31 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20230531_0015'),
        ('sales', '0007_rename_invetory_sales_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.iventory'),
        ),
    ]