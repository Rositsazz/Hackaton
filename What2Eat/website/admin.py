from django.contrib import admin
from .models import User, ProductToBuy, Recipe, Shop, LastCookedRecipe, UserCard


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prepare_time', 'servings')
    list_filter = ('prepare_time',)
    search_fields = ['name']


admin.site.register(User)
admin.site.register(ProductToBuy)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Shop)
admin.site.register(LastCookedRecipe)
admin.site.register(UserCard)
