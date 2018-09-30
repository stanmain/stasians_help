# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The mixins module from the news app."""

from django.views.generic.base import ContextMixin

from .models import New


class LatestNewsMixin(ContextMixin):
    """Mixin of category list."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.order_by('-pubdate')[:5]
        return context
