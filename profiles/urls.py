# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The urls module from the profiles app."""

from django.urls import path

from .views import ProfileView, UserProfileView, UserEditView, ProfileEditView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('edit/user/', UserEditView.as_view(), name='user_edit'),
    path('edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('user/<str:slug>/', UserProfileView.as_view(), name='profiles'),
]
