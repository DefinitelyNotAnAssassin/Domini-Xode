# Generated by Django 3.2.6 on 2023-11-03 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0009_alter_announcements_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/static/domini_xode_logo.jpg', null=True, upload_to='static/'),
        ),
    ]
