# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150527_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='prepare_time',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
