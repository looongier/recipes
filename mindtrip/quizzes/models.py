#!/usr/bin/env python
# encoding: utf-8

import os

from django.db import models

from .helpers import slugify


def photo_upload_to(instance, filename):
    return os.sep.join(
        ['recipes', str(instance.recipe_id), filename])


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nazwa')
    short = models.CharField(max_length=255, verbose_name='Czas przygotowania')
    description = models.TextField(verbose_name='Opis')
    added_at = models.DateField(verbose_name='Data dodania')

    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Tagi')

    class Meta:
        verbose_name = 'Przepis'
        verbose_name_plural = 'Przepisy'

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(
        upload_to=photo_upload_to, verbose_name='Zdjęcie')
    recipe = models.ForeignKey(
        Recipe, verbose_name='Przepis', related_name='photos',
        on_delete=models.CASCADE)
    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Opis')

    class Meta:
        verbose_name = 'Zdjęcie'
        verbose_name_plural = 'Zdjęcia'

    def __str__(self):
        return '{0} ({1})'.format(self.recipe, self.photo.url)


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Nazwa')
    slug = models.CharField(max_length=255, blank=True, verbose_name='Slug')

    class Meta:
        abstract = False
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagi'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(
            force_insert=force_insert, force_update=force_update,
            using=using, update_fields=update_fields)
