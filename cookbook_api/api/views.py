from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers import RecipeSerializer
from recipes.models import Recipe, RecipeProduct, Product


@api_view(['GET'])
def add_product_to_recipe(request):
    if (
        'recipe_id' not in request.GET or
        'product_id' not in request.GET or
        'weight' not in request.GET
    ):
        return Response(
            {'В запросе должны быть параметры recipe_id, product_id, weight'},
            status=status.HTTP_400_BAD_REQUEST
        )
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    recipe_product = RecipeProduct.objects.filter(
        recipe=recipe,
        product=product
    )
    if recipe_product:
        recipe_product.update(weight=F('weight')+weight)
    else:
        recipe_product = RecipeProduct.objects.create(
            recipe=recipe,
            product=product,
            weight=weight
        )
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def cook_recipe(request):
    pass
