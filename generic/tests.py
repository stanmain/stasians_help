# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The tests module from the generic app."""

from django.conf import settings
from django.urls import reverse


class LoginForTestMixin:
    """The mixin for authorization in test."""

    default_login = True

    def login(self):
        """Administrator authorization."""
        self.client.login(
            username=settings.TEST_USERNAME,
            password=settings.TEST_PASSWORD
        )


class ViewTestMixin:
    """
    The mixin for testing view.

    Need define variables:
    `url_at_location` - url of the page;
    `url_by_name` - reverse url of the page;
    `template` - path to template.
    """

    def test_view_url_at_location(self):
        try:
            if self.default_login:
                self.login()
        except AttributeError:
            pass
        response = self.client.get(self.url_at_location)
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        try:
            if self.default_login:
                self.login()
        except AttributeError:
            pass
        response = self.client.get(self.url_by_name)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        try:
            if self.default_login:
                self.login()
        except AttributeError:
            pass
        response = self.client.get(self.url_by_name)
        self.assertTemplateUsed(response, self.template)


class AdminTestMixin(LoginForTestMixin):
    """
    The mixin test for admin model.

    Need define variables:
    `model` - registered model;
    `object_id` - object slug.
    """

    @property
    def info(self):
        return self.model._meta.app_label, self.model._meta.model_name

    def test_changelist(self):
        self.login()
        response = self.client.get(
            reverse('admin:%s_%s_changelist' % self.info))
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        self.login()
        response = self.client.get(
            reverse('admin:%s_%s_add' % self.info))
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        self.login()
        response = self.client.get(
            reverse(
                'admin:%s_%s_history' % self.info,
                kwargs={'object_id': self.object_id}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.login()
        response = self.client.get(
            reverse(
                'admin:%s_%s_delete' % self.info,
                kwargs={'object_id': self.object_id}
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_change(self):
        self.login()
        response = self.client.get(
            reverse(
                'admin:%s_%s_change' % self.info,
                kwargs={'object_id': self.object_id}
            )
        )
        self.assertEqual(response.status_code, 200)
