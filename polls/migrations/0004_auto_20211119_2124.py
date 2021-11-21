# Generated by Django 3.1.7 on 2021-11-19 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=250, verbose_name='Telebe Adi')),
                ('title', models.CharField(max_length=1000, verbose_name='Telebenin reyi')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.RemoveField(
            model_name='blog',
            name='subject',
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(help_text='Her Categoryden sonra - qoyun', max_length=1000, null=True, verbose_name='Kategoriya'),
        ),
    ]
