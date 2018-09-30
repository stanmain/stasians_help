# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test views from the subjects app."""

from django.test import TestCase
from django.urls import reverse
from generic.tests import ViewTestMixin
from ..models import Subject


class CategoryViewTest(TestCase, ViewTestMixin):
    """Tests for CategoryView."""

    fixtures = ['dump.json']
    template = 'subjects/category.html'
    url_at_location = '/subjects/laboratory/'

    @property
    def url_by_name(self):
        return self.get_url('laboratory')

    def get_url(self, slug: str):
        """Get view url by name."""
        return reverse('category', kwargs={'slug': slug})

    def test_view_pagination(self):
        response = self.client.get(self.get_url('laboratory'))
        self.assertIn('is_paginated', response.context)
        self.assertFalse(response.context['is_paginated'])

    def test_context_contains_category(self):
        response = self.client.get(self.get_url('laboratory'))
        self.assertIn('category', response.context)
        self.assertEqual('laboratory', response.context['category'].slug)

    def test_context_contains_subjects(self):
        response = self.client.get(self.get_url('laboratory'))
        self.assertIn('subjects', response.context)
        python = Subject.objects.get(name='Python')
        cpp = Subject.objects.get(name='C++')
        arduino = Subject.objects.get(name='Arduino')
        self.assertIn(python, response.context['subjects'])
        self.assertIn(cpp, response.context['subjects'])
        self.assertNotIn(arduino, response.context['subjects'])

    def test_context_contains_subjects_with_status_false(self):
        response = self.client.get(self.get_url('course'))
        arduino = Subject.objects.get(name='Arduino')
        self.assertNotIn(arduino, response.context['subjects'])


class SubjectDetailViewTest(TestCase, ViewTestMixin):
    """Tests for SubjectDetailView."""

    fixtures = ['dump.json']
    template = 'subjects/detail.html'
    url_at_location = '/subjects/1/'

    @property
    def url_by_name(self):
        return self.get_url(1)

    def get_url(self, slug: int):
        """Get view url by name."""
        return reverse('subjects_detail', kwargs={'slug': slug})

    def test_context_contains_subject(self):
        response = self.client.get(self.get_url(1))
        self.assertIn('subject', response.context)
        subject = Subject.objects.get(id=1)
        self.assertEqual(subject, response.context['subject'])

    def test_view_subject_not_enabled(self):
        response = self.client.get(self.get_url(3))
        self.assertEqual(response.status_code, 404)


class SubjectListViewTest(TestCase, ViewTestMixin):
    """Tests for SubjectListView."""
    fixtures = ['dump.json']
    template = 'subjects/list.html'
    url_at_location = '/subjects/'

    @property
    def url_by_name(self):
        return self.get_url()

    def get_url(self):
        """Get view url by name."""
        return reverse('subjects_list')

    def test_context_contains_subjects(self):
        response = self.client.get(self.get_url())
        self.assertIn('subjects', response.context)
        python = Subject.objects.get(id=1)
        cpp = Subject.objects.get(id=2)
        arduino = Subject.objects.get(id=3)
        self.assertIn(python, response.context['subjects'])
        self.assertIn(cpp, response.context['subjects'])
        self.assertNotIn(arduino, response.context['subjects'])
