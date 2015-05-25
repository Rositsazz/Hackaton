# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LastCookedRecipe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('amount', models.FloatField()),
                ('barcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('prepare_time', models.PositiveSmallIntegerField()),
                ('total_fat', models.FloatField()),
                ('protein', models.FloatField()),
                ('servings', models.PositiveSmallIntegerField()),
                ('directions', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='')),
                ('products', models.ForeignKey(to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('shop_name', models.CharField(max_length=50)),
                ('barcode_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_kilos', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(200)])),
                ('gender', models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female')])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('height', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(240)])),
                ('favourite_repice', models.ForeignKey(to='website.Recipe')),
                ('fridge', models.ForeignKey(to='website.Product')),
                ('last_cooked_recipe', models.ForeignKey(to='website.LastCookedRecipe')),
                ('shops', models.ForeignKey(to='website.Shop')),
            ],
        ),
        migrations.AddField(
            model_name='lastcookedrecipe',
            name='recipe_id',
            field=models.ForeignKey(to='website.Recipe'),
        ),
        migrations.AddField(
            model_name='lastcookedrecipe',
            name='user_id',
            field=models.ForeignKey(to='website.User'),
        ),
    ]
