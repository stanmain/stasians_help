# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test mixins from the subjects app."""

from django.test import TestCase
from ..models import Subject
from ..mixins import ExpectedSubjectMixin, PopularSubjectMixin


class ExpectedSubjectMixinTest(TestCase):
    """Tests for ExpectedSubjectMixin."""
    fixtures = ['dump.json']

    def test_context_contains_subjects(self):
        context = ExpectedSubjectMixin().get_context_data()
        self.assertIn('expected_subjects', context)
        arduino = Subject.objects.get(pk=3)
        self.assertIn(arduino, context['expected_subjects'])


class PopularSubjectMixinTest(TestCase):
    """Tests for PopularSubjectMixin."""
    fixtures = ['dump.json']

    def test_context_contains_subjects(self):
        context = PopularSubjectMixin().get_context_data()
        self.assertIn('popular_subjects', context)
        python = Subject.objects.get(pk=1)
        self.assertIn(python, context['popular_subjects'])
        cpp = Subject.objects.get(pk=2)
        self.assertIn(cpp, context['popular_subjects'])
        arduino = Subject.objects.get(pk=3)
        self.assertNotIn(arduino, context['popular_subjects'])
