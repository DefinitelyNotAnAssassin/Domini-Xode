# Generated by Django 3.2.6 on 2023-10-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0003_auto_20231030_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='thumbnail',
            field=models.ImageField(blank=True, default='static/img/domini_xode_logo.jpg', null=True, upload_to='static/img/'),
        ),
    ]