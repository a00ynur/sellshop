# Generated by Django 4.0.4 on 2022-09-09 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tag_alter_blog_options_remove_blog_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
