# Generated by Django 3.1.6 on 2021-02-06 22:02

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='cart',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
