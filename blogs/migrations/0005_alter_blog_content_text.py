# Generated by Django 4.0.6 on 2022-07-18 13:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_user_id_blog_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
