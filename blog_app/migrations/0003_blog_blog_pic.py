# Generated by Django 5.1.5 on 2025-01-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_rename_user_comment_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_pic',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pics/'),
        ),
    ]
