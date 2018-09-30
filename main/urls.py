# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the main app."""

from django.urls import path

from .views import MainPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
]
