# Generated by Django 2.0 on 2018-12-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20181222_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_img',
            field=models.ImageField(blank=True, upload_to='img/%Y%m', verbose_name='歌曲图片'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_lyrics',
            field=models.FileField(blank=True, upload_to='file/%Y%m', verbose_name='歌词'),
        ),
    ]