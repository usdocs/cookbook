from django.urls import path

from api import views

urlpatterns = [
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
