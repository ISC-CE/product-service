# Generated by Django 4.2.6 on 2023-10-26 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0002_productcategory_productimage_productinventory_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='ProductInventory',
        ),
        migrations.DeleteModel(
            name='ProductManufacturers',
        ),
    ]