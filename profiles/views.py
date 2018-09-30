# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the profiles app."""

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy

from orders.mixins import OrderListMixin
from .forms import ExUserCreationForm
from .models import Profile, ExUser


class RegistrationView(FormView):
    """View of registration of a new user."""

    form_class = ExUserCreationForm
    success_url = reverse_lazy('profile_edit')
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView, OrderListMixin):
    """View of user profile."""

    model = ExUser
    template_name = 'profiles/profile.html'
    context_object_name = 'object'

    def get_object(self):
        return self.request.user


class UserProfileView(DetailView, OrderListMixin):
    """View of other user profile."""

    model = ExUser
    template_name = 'profiles/profile.html'
    slug_field = 'username'
    context_object_name = 'object'


class UserEditView(LoginRequiredMixin, UpdateView):
    """View of user edit."""

    model = ExUser
    fields = ('username', 'email')
    template_name = 'profiles/edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """View of profile edit."""

    model = Profile
    fields = ('first_name', 'last_name', 'bio', 'location', 'birth_date')
    template_name = 'profiles/edit.html'

    def get_object(self):
        return self.request.user.profile
