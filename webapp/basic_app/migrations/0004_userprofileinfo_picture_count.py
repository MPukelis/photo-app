# Generated by Django 2.0.5 on 2018-08-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_remove_userprofileinfo_portfolio_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='picture_count',
            field=models.IntegerField(default=24),
        ),
    ]