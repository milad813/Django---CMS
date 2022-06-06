# Generated by Django 4.0.4 on 2022-06-02 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_rename_author_id_posts_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='my_app.tag'),
        ),
    ]
