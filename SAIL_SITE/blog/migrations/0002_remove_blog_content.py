# Generated by Django 3.2.4 on 2021-12-28 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
