# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the subjects app."""

from django.urls import path

from .views import SubjectListView, SubjectDetailView, CategoryView


urlpatterns = [
    path('', SubjectListView.as_view(), name='subjects_list'),
    path('<int:slug>/', SubjectDetailView.as_view(), name='subjects_detail'),
    path('<str:slug>/', CategoryView.as_view(), name='category'),
]
