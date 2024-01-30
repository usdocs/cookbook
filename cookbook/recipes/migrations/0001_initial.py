# Generated by Django 3.2.16 on 2024-01-30 17:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название продукта')),
                ('cooked_dishes', models.PositiveSmallIntegerField(default=0, verbose_name='Количество приготовленных блюд')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название рецепта')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecipeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32000)], verbose_name='Вес продукта в граммах')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_recipe', to='recipes.product', verbose_name='Продукт')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_product', to='recipes.recipe', verbose_name='Рецепт')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='product',
            field=models.ManyToManyField(related_name='products', through='recipes.RecipeProduct', to='recipes.Product', verbose_name='Используемые продукты в рецепте'),
        ),
        migrations.AddConstraint(
            model_name='recipeproduct',
            constraint=models.UniqueConstraint(fields=('product', 'recipe'), name='unique_recipe_product'),
        ),
    ]