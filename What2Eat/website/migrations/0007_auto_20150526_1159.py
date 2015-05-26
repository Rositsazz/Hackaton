# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150526_1159'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_cards',
            new_name='User_card',
        ),
    ]
