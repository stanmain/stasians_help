# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The tests module from the pages app."""

from django.test import TestCase
from django.urls import reverse
from generic.tests import ViewTestMixin


class AboutViewTest(TestCase, ViewTestMixin):
    """Tests for AboutView."""

    template = 'pages/about.html'
    url_at_location = '/pages/about/'
    url_by_name = reverse('about')


class ContactsViewTest(TestCase, ViewTestMixin):
    """Tests for ContactsView."""

    template = 'pages/contacts.html'
    url_at_location = '/pages/contacts/'
    url_by_name = reverse('contacts')


class PaymentViewTest(TestCase, ViewTestMixin):
    """Tests for PaymentView."""

    template = 'pages/payment.html'
    url_at_location = '/pages/payment/'
    url_by_name = reverse('payment')
