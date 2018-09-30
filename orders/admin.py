# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The admin module from the orders app."""

from django.contrib import admin

from .models import Order, Statement


class StatementInline(admin.TabularInline):
    """"""
    model = Statement
    fields = ('date', 'amount', 'description')
    readonly_fields = ('date', 'amount', 'description')
    exclude = ('terminal',)
    min_num = 0
    max_num = 0


class CategoryListFilter(admin.SimpleListFilter):
    """"""
    title = 'Категории'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return ((1, 'one'), (2, 'two'))

    def queryset(self, request, queryset):
        if self.value() == 1:
            return queryset.filter(subject__category__pk=1)
        if self.value() == 2:
            return queryset.filter(subject__category__pk=2)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """"""
    model = Order
    list_display = ('id', 'pubdate', 'user', 'subject', 'status', 'price',
                    'prepayment', 'payment')
    list_display_links = ('id', 'pubdate')
    list_editable = ('status',)
    list_filter = ('status', 'pubdate', CategoryListFilter, 'subject')
    inlines = (StatementInline,)
    readonly_fields = ('payment',)
    date_hierarchy = 'pubdate'


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    """"""
    list_display = ('date', 'amount', 'terminal', 'description')
    # list_display_links = ('date', 'terminal', 'description')
    list_filter = ('date',)
    search_fields = ('terminal', 'description')
