# Generated by Django 4.0.4 on 2022-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_remove_posts_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author_id',
            field=models.IntegerField(default=1),
        ),
    ]