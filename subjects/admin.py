# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The admin module from the subjects app."""

from django.contrib import admin

from .models import Subject, Category


admin.site.register(Subject)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
