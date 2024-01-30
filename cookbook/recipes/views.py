from django.shortcuts import get_object_or_404, render
from django.db.models import F, Q

from recipes.models import Recipe, RecipeProduct, Product


def show_recepes_without_product(request):
    template = 'show_recepes_without_product.html'
    if 'product_id' not in request.GET:
        context = {
            'request': 'В запросе должны быть параметры product_id',
        }
        return render(request, template, context)
    product = get_object_or_404(Product, id=request.GET.get('product_id'))

    recipes_list = Recipe.objects.filter(
        ~Q(
            recipe_product__product=product
        ) | Q(
            recipe_product__weight__lt=10,
            recipe_product__product=product
        )
    )
    context = {
        'product': product,
        'recipes_list': recipes_list,
    }
    return render(request, template, context)


def add_product_to_recipe(request):
    template = 'add_product_to_recipe.html'
    if (
        'recipe_id' not in request.GET or
        'product_id' not in request.GET or
        'weight' not in request.GET
    ):
        context = {
            'request': 'В запросе должны быть параметры recipe_id, '
                       'product_id, weigh',
        }
        return render(request, template, context)
    recipe = get_object_or_404(Recipe, id=request.GET.get('recipe_id'))
    product = get_object_or_404(Product, id=request.GET.get('product_id'))
    weight = request.GET.get('weight')
    recipe_product = RecipeProduct.objects.filter(
        recipe=recipe,
        product=product
    )
    if recipe_product:
        recipe_product.update(weight=weight)
        recipe_product = recipe_product.first()
    else:
        recipe_product = RecipeProduct.objects.create(
            recipe=recipe,
            product=product,
            weight=weight
        )
    context = {
        'product': product,
        'recipe_product': recipe_product,
        'recipe': recipe,
    }
    return render(request, template, context)


def cook_recipe(request):
    template = 'cook_recipe.html'
    if 'recipe_id' not in request.GET:
        context = {
            'request': 'В запросе должны быть параметры recipe_id',
        }
        return render(request, template, context)
    recipe = get_object_or_404(Recipe, id=request.GET.get('recipe_id'))
    Product.objects.filter(
        product_recipe__recipe=recipe
    ).update(cooked_dishes=F('cooked_dishes')+1)
    product_list = Product.objects.filter(product_recipe__recipe=recipe)
    context = {
        'recipe': recipe,
        'product_list': product_list,
    }
    return render(request, template, context)
