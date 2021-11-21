# Generated by Django 3.2.9 on 2021-11-18 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211118_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=1000, null=True, verbose_name='Kategoriya')),
                ('head', models.CharField(max_length=250, null=True, verbose_name='Baslig')),
                ('subject', models.TimeField()),
                ('image', models.ImageField(blank=True, upload_to='polls/%Y/%M/%D/%H/%M/%S', verbose_name='Image')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('click', models.IntegerField(default=0, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
