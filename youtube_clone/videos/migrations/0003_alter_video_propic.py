# Generated by Django 4.2.5 on 2023-09-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='propic',
            field=models.ImageField(null=True, upload_to='propic/'),
        ),
    ]