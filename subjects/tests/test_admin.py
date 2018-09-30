# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test admin from the subjects app."""

from django.test import TestCase
from generic.tests import AdminTestMixin
from ..models import Subject, Category


class CategoryAdminTest(AdminTestMixin, TestCase):
    """Tests for Category admin."""
    fixtures = ['dump.json']
    model = Category
    object_id = 1


class SubjectAdminTest(AdminTestMixin, TestCase):
    """Tests for Subject admin."""
    fixtures = ['dump.json']
    model = Subject
    object_id = 1
