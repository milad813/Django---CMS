# Generated by Django 4.0.4 on 2022-06-02 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0012_remove_posts_comments_posts_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='text',
            new_name='content',
        ),
    ]