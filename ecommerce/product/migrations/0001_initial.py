# Generated by Django 3.1.6 on 2021-03-25 17:28

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_descrption', models.TextField(blank=True, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('product_discount', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=9, null=True)),
                ('product_discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Lenovo\\Desktop\\SecondStagePragmatech\\My_Ecommerce_Project\\ecommerce\\media'), upload_to=product.models.upload_product_file_loc)),
                ('product_stock', models.BooleanField(default=False)),
                ('product_title', models.TextField(blank=True, null=True)),
                ('product_vip', models.BooleanField(default=False)),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Lenovo\\Desktop\\SecondStagePragmatech\\My_Ecommerce_Project\\static_cdn\\product_media'), upload_to=product.models.upload_product_file_loc)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
