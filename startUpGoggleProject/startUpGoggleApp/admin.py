# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.contrib import admin



# Register your models here.

def make_deactive(self, request, queryset):
    queryset.update(isActive='False')


def make_active(self, request, queryset):
    queryset.update(isActive='True')


make_deactive.short_description = "Deactivate Selected Item"
make_active.short_description = "activate Selected Item"


class BusinessTypeAdmin(admin.ModelAdmin):
    search_fields = ['title', 'publish', 'isActive']
    list_display = ['title', 'publish', 'isActive']
    actions = [make_deactive, make_active]

class BusinessDirectoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'publish', 'isActive']
    list_display = ['name', 'publish', 'isActive']
    actions = [make_deactive, make_active]

class BusinessNewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'publish', 'isActive']
    list_display = ['title', 'publish', 'isActive']
    actions = [make_deactive, make_active]

admin.site.register(BusinessType, BusinessTypeAdmin)
admin.site.register(BusinessDirectory, BusinessDirectoryAdmin)
admin.site.register(BusinessNews, BusinessNewsAdmin)
