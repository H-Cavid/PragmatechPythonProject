# Generated by Django 3.2.5 on 2021-08-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]