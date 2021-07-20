# Generated by Django 2.2.12 on 2021-07-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='bg_image_id',
        ),
        migrations.AddField(
            model_name='event',
            name='bg_image_id',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='yt_link',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
