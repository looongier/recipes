#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import render_to
from django.shortcuts import get_object_or_404

from .models import Quiz, Tag


@render_to('quizzes/recipes.html')
def get_recipes(request):
    return {'recipes': Quiz.objects.all().order_by('-added_at')}


@render_to('quizzes/quiz.html')
def get_quiz(request, quiz_id):
    return {'quiz': get_object_or_404(Quiz, id=quiz_id)}


@render_to('quizzes/tags.html')
def get_tags(request):
    return {'tags': Tag.objects.all()}