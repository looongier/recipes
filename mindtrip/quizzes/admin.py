#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin

from .models import Photo, Recipe, Tag

admin.site.register(Recipe)
admin.site.register(Photo)
admin.site.register(Tag)
