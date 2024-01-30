from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from recipes.models import Product, Recipe


def show_recepes_without_product(request):
    template = 'product/product_detail.html'
    if 'product_id' not in request.GET:
        context = {
            'request': 'В запросе должны быть параметры recipe_id, '
                       'product_id, weigh',
        }
        return render(request, template, context)
    product = get_object_or_404(Product, id=request.GET.get('product_id'))
    recipes_list = Recipe.objects.filter(
            Q(
                ingredients__amount__lt=10,
                ingredients__id=request.GET.get('product_id')
            ) | ~Q(ingredients__id=request.GET.get('product_id'))
        )
    context = {
        'product': product,
        'recipes_list': recipes_list,
    }
    return render(request, template, context)
