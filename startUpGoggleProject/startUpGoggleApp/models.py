# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models
from datetime import datetime
from constant import FONT, BACK

from multiselectfield import MultiSelectField

class StartUpType(models.Model):
    title = models.CharField(max_length=200)
    publish = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField(default='False')

    def __unicode__(self):
        return self.title


class StartupDirectorie(models.Model):
    type = models.ManyToManyField(StartUpType)
    name = models.CharField(max_length=200)
    introduction_text = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = "static/directory/")
    background_color = models.CharField(max_length=50, choices=BACK)
    font_color = models.CharField(max_length=50, choices=FONT)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    youtube = models.CharField(max_length=300)
    linkedin = models.CharField(max_length=300)
    publish = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField(default='True')

class StartUpNew(models.Model):
    type = models.ManyToManyField(StartUpType)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True)
    intro_text = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="static/news/")
    background_color = models.CharField(max_length=50, choices=BACK)
    font_color = models.CharField(max_length=50, choices=FONT)
    publish = models.DateTimeField(default=datetime.now)
    isActive = models.BooleanField(default='True')