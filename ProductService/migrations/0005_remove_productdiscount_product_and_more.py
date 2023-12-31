# Generated by Django 4.2.6 on 2023-11-02 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductService', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdiscount',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productrecommendation',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='product',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductDiscount',
        ),
        migrations.DeleteModel(
            name='ProductManufacturer',
        ),
        migrations.DeleteModel(
            name='ProductRecommendation',
        ),
        migrations.DeleteModel(
            name='ProductVariation',
        ),
    ]
