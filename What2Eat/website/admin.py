from django.contrib import admin
from .models import User, Product, Recipe, Shop, LastCookedRecipe


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(Shop)
admin.site.register(LastCookedRecipe)
