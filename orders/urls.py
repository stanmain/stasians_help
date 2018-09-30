# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the orders app."""

from django.urls import path

from .views import (OrderListView, OrderDetailView, OrderCreateView,
                    OrderCancelView)


urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('<int:slug>/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:slug>/cancel/', OrderCancelView.as_view(), name='order_cancel'),
    path(
        'subject/<int:slug>/',
        OrderCreateView.as_view(),
        name='order_create'
    ),
]
