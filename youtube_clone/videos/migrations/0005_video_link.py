# Generated by Django 4.2.5 on 2023-09-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_remove_video_propic_video_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]