# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150525_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductToBuy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=70)),
                ('amount', models.FloatField()),
                ('product_brand', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_cards',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='directions',
            new_name='instructions',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='barcode_length',
            new_name='card_barcode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favourite_repice',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fridge',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_cooked_recipe',
        ),
        migrations.AddField(
            model_name='shop',
            name='card_barcode_length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepare_time',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='user_cards',
            name='shop_id',
            field=models.ForeignKey(to='website.Shop'),
        ),
        migrations.AddField(
            model_name='user_cards',
            name='user_id',
            field=models.ForeignKey(to='website.User'),
        ),
        migrations.AddField(
            model_name='producttobuy',
            name='shop_id',
            field=models.ForeignKey(to='website.Shop'),
        ),
    ]
