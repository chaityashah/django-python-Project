# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.CharField(default='Windsor', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.CharField(default='Canada', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='pubyear',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='textbook',
            field=models.ForeignKey(to='myapp.Book'),
        ),
    ]
