#!/usr/bin/env python
# encoding: utf-8

from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.get_recipes, name='recipes'),
    path('<int:quiz_id>', views.get_quiz, name='quiz'),
    path('gwara',
         TemplateView.as_view(template_name='quizzes/gwara.html'), name='dialect'),
]
