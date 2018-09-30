# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The forms module from the profiles app."""

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import EmailField

from .models import ExUser


class ExUserCreationForm(UserCreationForm):
    """Form to create a new user."""

    class Meta:
        model = ExUser
        fields = ('username', 'email')
        field_classes = {'username': UsernameField, 'email': EmailField}


# class ProfileEditForm(forms.ModelForm):
#     """"""

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ('user',)
