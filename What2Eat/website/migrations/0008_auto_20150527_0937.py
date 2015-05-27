# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20150526_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteRepice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('recipe', models.ForeignKey(to='website.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('card_barcode', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_card',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='user_card',
            name='user_id',
        ),
        migrations.RenameField(
            model_name='lastcookedrecipe',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='lastcookedrecipe',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='producttobuy',
            old_name='shop_id',
            new_name='shop',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_kilos',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='card_barcode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shops',
        ),
        migrations.AddField(
            model_name='producttobuy',
            name='user',
            field=models.ForeignKey(to='website.User', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='User_card',
        ),
        migrations.AddField(
            model_name='usercard',
            name='shop',
            field=models.ForeignKey(to='website.Shop'),
        ),
        migrations.AddField(
            model_name='usercard',
            name='user',
            field=models.ForeignKey(to='website.User'),
        ),
        migrations.AddField(
            model_name='favouriterepice',
            name='user',
            field=models.ForeignKey(to='website.User'),
        ),
    ]
