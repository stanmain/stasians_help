# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test admin from the profiles app."""

from django.test import TestCase
from generic.tests import AdminTestMixin
from ..models import ExUser


class ExUserAdminTest(AdminTestMixin, TestCase):
    """Tests for Category admin."""
    fixtures = ['dump.json']
    model = ExUser
    object_id = 1
