# Generated by Django 3.1.6 on 2021-03-01 19:29

from django.db import migrations, models


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
    ]
