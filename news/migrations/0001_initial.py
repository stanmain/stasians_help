# Generated by Django 2.1 on 2018-09-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, unique_for_date='update', verbose_name='Заголовок')),
                ('description', models.TextField(max_length=140, verbose_name='Описание')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('pubdate', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-pubdate'],
            },
        ),
    ]