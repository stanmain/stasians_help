# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The mixins module from the orders app."""

from django.views.generic.base import ContextMixin

from .models import Order


class OrderListMixin(ContextMixin):
    """Mixin of orders list."""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user == kwargs['object']:
            context['orders'] = Order.objects.filter(user=context['object'])
        return context
