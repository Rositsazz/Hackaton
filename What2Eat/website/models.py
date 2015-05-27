from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female')
        )
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(blank=True, max_length=20)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_TYPES)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    height = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(240)])
    weight = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(200)])

    def __str__(self):
        return self.username


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    products = models.CharField(max_length=1000)
    prepare_time = models.CharField(max_length=15)
    instructions = models.CharField(max_length=5000)
    image = models.CharField(max_length=300)
    total_fat = models.FloatField()
    protein = models.FloatField()
    servings = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)


class LastCookedRecipe(models.Model):
    user = models.ForeignKey('User')
    recipe = models.ForeignKey('Recipe')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.recipe_id.name


class FavouriteRepice(models.Model):
    user = models.ForeignKey('User')
    recipe = models.ForeignKey('Recipe')

    def __str__(self):
        return self.recipe.name


class ProductToBuy(models.Model):
    name = models.CharField(max_length=70)
    amount = models.FloatField()
    product_brand = models.CharField(blank=True, max_length=100)
    shop = models.ForeignKey('Shop')
    user = models.ForeignKey('User')

    def __str__(self):
        return self.name


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    card_barcode_length = models.IntegerField()

    def __str__(self):
        return self.shop_name


class UserCard(models.Model):
    user = models.ForeignKey('User')
    shop = models.ForeignKey('Shop')
    card_barcode = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.user.username, self.shop.shop_name)
