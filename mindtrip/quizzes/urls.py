#!/usr/bin/env python
# encoding: utf-8

from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.get_recipes, name='recipes'),
    path('<int:recipe_id>', views.get_recipe, name='recipe'),
    path('gwara', TemplateView.as_view(template_name='recipes/gwara.html'), name='dialect'),
    path('tagi', views.get_tags, name='tags'),
    path('tagi/<slug:slug>', views.get_tag, name='tag'),

]
