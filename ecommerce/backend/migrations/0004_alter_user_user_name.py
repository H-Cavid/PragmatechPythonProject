# Generated by Django 3.2.5 on 2021-08-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]
