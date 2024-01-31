from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=200,
        unique=True,
    )
    cooked_dishes = models.PositiveSmallIntegerField(
        'Количество приготовленных блюд',
        default=0,
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(
        'Название рецепта',
        max_length=256,
    )

    product = models.ManyToManyField(
        Product,
        through='RecipeProduct',
        related_name='products',
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
        related_name='product_recipe',
        verbose_name='Продукт'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_product',
        verbose_name='Рецепт'
    )
    weight = models.PositiveSmallIntegerField(
        'Вес продукта в граммах',
        default=0,
        validators=[
            MaxValueValidator(settings.MAX_VALUE)
        ],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'recipe'],
                name='unique_recipe_product'
            )
        ]
        ordering = ['-id']

    def __str__(self):
        return f'{self.product} {self.recipe}'
