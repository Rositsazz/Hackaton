# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150527_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='healthy_coef',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='keywords',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
