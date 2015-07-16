# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150528_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('subject', models.CharField(max_length=100, unique=True)),
                ('intro_course', models.BooleanField(default=True)),
                ('time', models.IntegerField(choices=[(0, 'No preference'), (1, 'Morning'), (2, 'Afternoon'), (3, 'Evening')], default=0)),
                ('num_responses', models.IntegerField(default=0)),
                ('avg_age', models.IntegerField(default=20)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(default='1991-01-31'),
        ),
    ]
