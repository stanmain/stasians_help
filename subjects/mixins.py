# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The mixins module from the subjects app."""

from django.db import models
from django.views.generic.base import ContextMixin

from .models import Subject


class ExpectedSubjectMixin(ContextMixin):
    """Mixin of expected subject."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expected_subjects'] = Subject.objects.filter(
            status=Subject.STATUS_EXPECTED
        ).order_by(
            'update'
        )[0:3]
        return context


# class CategoryListMixin(ContextMixin):
#     """Mixin of category list."""

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.filter(
#             status=True
#         ).exclude(
#             slug='other'
#         )
#         context['other_category'] = Category.objects.get(slug='other')
#         return context


class PopularSubjectMixin(ContextMixin):
    """Mixin of popular subject."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_subjects'] = Subject.objects.filter(
            status=Subject.STATUS_ENABLED
        ).annotate(
            orders_count=models.Count('order')
        ).order_by(
            '-orders_count',
            'name'
        )[:5]
        return context
