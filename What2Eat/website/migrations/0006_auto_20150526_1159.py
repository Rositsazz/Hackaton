# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150526_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttobuy',
            name='product_brand',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
