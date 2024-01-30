from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from recipes.models import Recipe, RecipeProduct


class RecipeProductSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='product.name')
    weigth = serializers.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_VALUE),
            MaxValueValidator(settings.MAX_VALUE)
        ]
    )

    class Meta:
        model = RecipeProduct
        fields = ('name', 'weigth')


class RecipeSerializer(serializers.ModelSerializer):

    products = RecipeProductSerializer(
        source='recipe_product',
        many=True,
    )

    class Meta:
        model = Recipe
        fields = ('products', 'name')
