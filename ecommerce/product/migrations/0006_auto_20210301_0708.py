# Generated by Django 3.1.5 on 2021-03-01 03:08

import django.core.files.storage
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\User\\Desktop\\PragmatechPythonProject\\ecommerce\\media'), upload_to=product.models.upload_product_file_loc),
        ),
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\User\\Desktop\\PragmatechPythonProject\\static_cdn\\product_media'), upload_to=product.models.upload_product_file_loc),
        ),
    ]
