#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import render_to
from django.shortcuts import get_object_or_404

from .models import Recipe, Tag


@render_to('recipes/recipes.html')
def get_recipes(request):
    return {'recipes': Recipe.objects.all().order_by('-added_at')}


@render_to('recipes/recipe.html')
def get_recipe(request, recipe_id):
    return {'recipe': get_object_or_404(Recipe, id=recipe_id)}


@render_to('recipes/tags.html')
def get_tags(request):
    return {'tags': Tag.objects.all()}


@render_to('recipes/tag.html')
def get_tag(request, slug):
    return {'recipes': Recipe.objects.filter(tags__slug=slug)}

@render_to('recipes/tiles.html')
def get_tiles(request):
    return {'recipes': Recipe.objects.all().order_by('-added_at')}