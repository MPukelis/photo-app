# Generated by Django 2.0.5 on 2018-08-07 13:26

import basic_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20180804_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicturecount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=basic_app.models.UserProfileInfo.get_upload_path),
        ),
    ]
