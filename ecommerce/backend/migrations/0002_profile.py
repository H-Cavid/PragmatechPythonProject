# Generated by Django 3.2.5 on 2021-08-11 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='userprofile.jpg', upload_to='UserProfile_pictures')),
                ('user_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('user_links', models.CharField(blank=True, max_length=50, null=True)),
                ('user_email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email.set()+', to=settings.AUTH_USER_MODEL)),
                ('user_phone_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone.set()+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
