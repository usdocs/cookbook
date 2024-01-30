from django.urls import path

from recipes import views

urlpatterns = [
    path(
        'show_recepes_without_product/',
        views.show_recepes_without_product,
        name='show_recepes_without_product'
     ),
]
