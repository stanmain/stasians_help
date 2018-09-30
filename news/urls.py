# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the news app."""

from django.urls import path

from .views import NewsDetailView, NewsListView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:slug>/', NewsDetailView.as_view(), name='news_detail'),
]
