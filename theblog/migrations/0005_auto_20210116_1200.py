# Generated by Django 3.1.4 on 2021-01-16 06:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0004_auto_20210107_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
