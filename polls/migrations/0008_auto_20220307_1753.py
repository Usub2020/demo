# Generated by Django 3.1.7 on 2022-03-07 17:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20211121_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='information',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
