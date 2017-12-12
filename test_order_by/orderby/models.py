# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Views(models.Model):
    tor = models.CharField(max_length=64)
    viewed_at = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    name = models.CharField(max_length=64)
    views = models.ManyToManyField(Views, related_name="article_views")
