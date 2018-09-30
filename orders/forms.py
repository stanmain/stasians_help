# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The forms module from the orders app."""

from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """Form for creating an order."""

    class Meta:
        model = Order
        fields = ('user', 'subject', 'description')
