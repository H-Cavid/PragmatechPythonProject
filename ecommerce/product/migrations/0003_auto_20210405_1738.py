# Generated by Django 3.1.5 on 2021-04-05 17:38

import django.core.files.storage
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210402_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/java/Desktop/sevil/NewProgmatechDjango/media'), upload_to=product.models.upload_product_file_loc),
        ),
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/java/Desktop/sevil/static_cdn/product_media'), upload_to=product.models.upload_product_file_loc),
        ),
    ]