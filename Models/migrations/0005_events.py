# Generated by Django 3.2.6 on 2023-10-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0004_alter_announcements_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=64)),
                ('event_description', models.CharField(max_length=1028)),
                ('event_start_date', models.DateTimeField()),
                ('event_end_date', models.DateTimeField()),
                ('event_location', models.CharField(max_length=32)),
                ('event_registration_link', models.CharField(blank=True, max_length=256, null=True)),
                ('event_flyer', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]