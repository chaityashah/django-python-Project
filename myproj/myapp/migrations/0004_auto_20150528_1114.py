# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150528_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='numpages',
            field=models.IntegerField(),
        ),
    ]
