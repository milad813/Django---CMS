# Generated by Django 4.0.4 on 2022-05-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_remove_posts_author_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='posts',
            name='images',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
