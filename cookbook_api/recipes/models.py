from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=200,
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200,
        default="г",
    )
    cooked_dishes = models.PositiveSmallIntegerField(
        'Количество приготовленных блюд',
        validators=[
            MinValueValidator(settings.MIN_VALUE),
        ],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='unique_measurement_unit_product'
            )
        ]
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    name = models.CharField(
        'Название рецепта',
        max_length=256,
    )

    ingredients = models.ManyToManyField(
        Product,
        through='RecipeProduct',
        related_name='product',
        verbose_name='Используемые продукты в рецепте'
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_product',
        verbose_name='Рецепт'
    )
    weight = models.PositiveSmallIntegerField(
        'Вес продукта',
        validators=[
            MinValueValidator(settings.MIN_VALUE),
            MaxValueValidator(settings.MAX_VALUE)
        ],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ingredient', 'recipe'],
                name='unique_recipe_ingredient'
            )
        ]
        ordering = ['-id']

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'
