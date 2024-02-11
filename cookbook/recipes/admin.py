from django.contrib import admin
from recipes.models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    min_num = 1
    extra = 0


class ListDisplayAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
    )


class RecipeAdmin(ListDisplayAdmin):
    inlines = (RecipeProductInline,)


admin.site.register(Product, ListDisplayAdmin)
admin.site.register(Recipe, RecipeAdmin)
