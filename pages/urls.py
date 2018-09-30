# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the pages app."""

from django.urls import path

from .views import AboutView, ContactsView, PaymentView


urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('payment/', PaymentView.as_view(), name='payment'),
]
