# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test views from the profiles app."""

from django.test import TestCase
from django.urls import reverse
from generic.tests import ViewTestMixin, LoginForTestMixin


class RegistrationViewTest(TestCase, ViewTestMixin):
    """Tests for RegistrationView."""

    fixtures = ['dump.json']
    template = 'registration/registration.html'
    url_at_location = '/registration/'
    url_by_name = reverse('registration')

    def test_view_authorized_user(self):
        self.assertTrue(
            self.client.login(username='tanya', password='359216qwerty'))
        response = self.client.get(self.url_by_name)
        self.client.logout()
        self.assertContains(response, 'Вы уже зарегистрированы.')


class ProfileViewTest(TestCase, ViewTestMixin, LoginForTestMixin):
    """Tests for ProfileView."""

    fixtures = ['dump.json']
    template = 'profiles/profile.html'
    url_at_location = '/profile/'
    url_by_name = reverse('profile')

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )


class UserProfileViewTest(TestCase, ViewTestMixin, LoginForTestMixin):
    """Tests for UserProfileView."""

    fixtures = ['dump.json']
    template = 'profiles/profile.html'
    url_at_location = '/profile/user/stan/'
    url_by_name = reverse('profiles', kwargs={'slug': 'stan'})

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertEqual(response.status_code, 200)


class UserEditViewTest(TestCase, ViewTestMixin, LoginForTestMixin):
    """Tests for UserEditView."""

    fixtures = ['dump.json']
    template = 'profiles/edit.html'
    url_at_location = '/profile/edit/user/'
    url_by_name = reverse('user_edit')

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )


class ProfileEditViewTest(TestCase, ViewTestMixin, LoginForTestMixin):
    """Tests for ProfileEditView."""

    fixtures = ['dump.json']
    template = 'profiles/edit.html'
    url_at_location = '/profile/edit/'
    url_by_name = reverse('profile_edit')

    def test_view_anonym_user(self):
        self.client.logout()
        response = self.client.get(self.url_by_name)
        self.assertRedirects(
            response,
            reverse('login') + f'?next={self.url_by_name}'
        )
