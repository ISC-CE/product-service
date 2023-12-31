# Generated by Django 4.2.6 on 2023-11-03 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0007_rename_product_inventory_product_stock_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductService.productinventory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
