# Generated by Django 4.1.7 on 2023-04-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_image_profile_attendance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
