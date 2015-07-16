# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150526_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
        migrations.RemoveField(
            model_name='author',
            name='city',
        ),
    ]
