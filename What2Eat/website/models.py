from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    products = models.ForeignKey('Product')
    prepare_time = models.PositiveSmallIntegerField()
    total_fat = models.FloatField()
    protein = models.FloatField()
    servings = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=5000)
    image = models.ImageField()


class Product(models.Model):
    name = models.CharField(max_length=70)
    amount = models.FloatField()
    barcode = models.CharField(max_length=20, default='0', editable=True)


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    barcode_length = models.IntegerField()


class LastCookedRecipe(models.Model):
    user_id = models.ForeignKey('User')
    recipe_id = models.ForeignKey('Recipe')
    date = models.DateField(auto_now=True)


class User(models.Model):
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female')
        )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    shops = models.ForeignKey('Shop')
    user_kilos = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(200)])
    gender = models.CharField(max_length=6, choices=GENDER_TYPES)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    height = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(240)])
    fridge = models.ForeignKey(Product)
    favourite_repice = models.ForeignKey('Recipe')
    last_cooked_recipe = models.ForeignKey('LastCookedRecipe')
