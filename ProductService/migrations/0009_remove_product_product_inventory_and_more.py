# Generated by Django 4.2.6 on 2023-11-03 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0008_product_product_inventory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_inventory',
        ),
        migrations.AddField(
            model_name='productinventory',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductService.product'),
        ),
    ]
