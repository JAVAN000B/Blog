# Generated by Django 3.0.6 on 2020-05-12 08:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
