# Generated by Django 3.1.5 on 2021-03-01 03:08

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
