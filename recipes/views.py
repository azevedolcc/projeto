from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.recipes.factory import make_recipe 

from .models import Recipe

# Create your views here. 
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
#        'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
    })


def category(request, category_id):
#    recipes = Recipe.objects.filter(category__id=category_id,is_published=True).order_by('-id')

#    category_name = getattr(
#        getattr(recipes.first(), 'category', None),
#        'name',
#        'not found'
#    )

#    if not recipes: 
#        return HttpResponse(content='Not found', status=404)
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id,is_published=True).order_by('-id')
    )

    return render(request, 'recipes/pages/Category.html', context={
#        'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes, 
        'title': f'{recipes[0].category.name} - Category | '
#       'title': f'{category_name} - Category | '
    })

def recipe(request, id):
#    recipe = Recipe.objects.filter(pk=id,is_published=True).order_by('-id').first()
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
