# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the pages app."""

from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    """A view for displaying the about page."""

    template_name = 'pages/about.html'


class ContactsView(TemplateView):
    """A view for displaying the contacts page."""

    template_name = 'pages/contacts.html'


class PaymentView(TemplateView):
    """A view for displaying the payment page."""

    template_name = 'pages/payment.html'
