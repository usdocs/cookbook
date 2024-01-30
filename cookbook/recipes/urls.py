from django.urls import path

from recipes import views

urlpatterns = [
    path(
        'show_recepes_without_product/',
        views.show_recepes_without_product,
        name='show_recepes_without_product'
    ),
    path(
        'add_product_to_recipe/',
        views.add_product_to_recipe,
        name='add_product_to_recipe'
    ),
    path(
        'cook_recipe/',
        views.cook_recipe,
        name='cook_recipe'
    ),
]
