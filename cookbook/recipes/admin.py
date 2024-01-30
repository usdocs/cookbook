from django.contrib import admin
from recipes.models import Product, Recipe, RecipeProduct


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeProduct
    min_num = 1
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)


admin.site.register(Product)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeProduct)
