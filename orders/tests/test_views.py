# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test_views module from the orders app."""

from django.test import TestCase
from django.urls import reverse
from generic.tests import ViewTestMixin, LoginForTestMixin
from subjects.models import Subject
from ..models import Order


class OrderListViewTest(ViewTestMixin, LoginForTestMixin, TestCase):
    """Tests for OrderListView."""

    fixtures = ['dump.json']
    template = 'orders/list.html'
    url_at_location = '/orders/'
    url_by_name = reverse('order_list')

    def test_view_pagination(self):
        self.login()
        response = self.client.get(self.url_by_name)
        self.assertIn('is_paginated', response.context)
        self.assertFalse(response.context['is_paginated'])

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )

    def test_context_contains_orders(self):
        self.login()
        response = self.client.get(self.url_by_name)
        orders = Order.objects.filter(user=response.context['user'])
        for order in orders:
            self.assertIn(order, response.context['orders'])


class OrderDetailViewTest(ViewTestMixin, LoginForTestMixin, TestCase):
    """Tests for OrderDetailView."""

    fixtures = ['dump.json']
    template = 'orders/detail.html'
    url_at_location = '/orders/1/'

    @property
    def url_by_name(self):
        return self.get_url(1)

    def get_url(self, slug: int):
        return reverse('order_detail', kwargs={'slug': slug})

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )

    def test_view_not_belonging_order(self):
        self.login()
        response = self.client.get(self.get_url(3))
        self.assertEqual(response.status_code, 404)

    def test_context_contains_order(self):
        self.login()
        response = self.client.get(self.url_by_name)
        order = Order.objects.get(pk=1)
        self.assertEqual(order, response.context['order'])


class OrderCreateViewTest(ViewTestMixin, LoginForTestMixin, TestCase):
    """Tests for OrderCreateView."""

    fixtures = ['dump.json']
    template = 'orders/create.html'
    url_at_location = '/orders/subject/1/'
    url_by_name = reverse('order_create', kwargs={'slug': 1})

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )

    def test_context_contains_correct_subject(self):
        self.login()
        response = self.client.get(self.url_by_name)
        subject = Subject.objects.get(pk=1)
        self.assertEqual(subject, response.context['subject'])


class OrderCancelViewTest(ViewTestMixin, LoginForTestMixin, TestCase):
    """Tests for OrderCancelView."""

    fixtures = ['dump.json']
    template = 'orders/cancel.html'
    url_at_location = '/orders/1/cancel/'

    @property
    def url_by_name(self):
        return self.get_url(1)

    def get_url(self, slug: int):
        return reverse('order_cancel', kwargs={'slug': slug})

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )

    def test_view_not_belonging_order(self):
        self.login()
        response = self.client.get(self.get_url(3))
        self.assertEqual(response.status_code, 404)
