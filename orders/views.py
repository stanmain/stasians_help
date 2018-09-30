# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the orders app."""

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from subjects.models import Subject
from .forms import OrderCreateForm
from .models import Order


class OrderListView(LoginRequiredMixin, ListView):
    """A view for displaying order list."""

    template_name = 'orders/list.html'
    paginate_by = 10
    context_object_name = 'orders'

    def get_queryset(self, **kwargs):
        return Order.objects.filter(
            user=self.request.user
        ).order_by('-pubdate')


class OrderDetailView(LoginRequiredMixin, DetailView):
    """A view for displaying order details."""

    model = Order
    template_name = 'orders/detail.html'
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().status != Order.STATUS_NEW:
            context['payment'] = self.get_object().statement_set.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            raise Http404
        return super().get(request, *args, **kwargs)


class OrderCreateView(LoginRequiredMixin, FormView):
    """A view for displaying order creation."""
    template_name = 'orders/create.html'

    form_class = OrderCreateForm
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['subject'] = self.kwargs['slug']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = Subject.objects.get(pk=self.kwargs['slug'])
        return context


class OrderCancelView(LoginRequiredMixin, UpdateView):
    """A view for displaying order cancelation."""

    template_name = 'orders/cancel.html'
    model = Order
    fields = ('status',)
    slug_field = 'pk'

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            raise Http404
        return super().get(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        if not self.get_object().can_canceled():
            raise Http404
        initial['status'] = Order.STATUS_CANCELED
        return initial
