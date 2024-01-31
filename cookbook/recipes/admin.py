from django.contrib import admin
from recipes.models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    min_num = 1
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeProductInline,)


admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
