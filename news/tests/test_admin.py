# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test admin from the news app."""

from django.test import TestCase
from generic.tests import AdminTestMixin
from ..models import New


class NewAdminTest(AdminTestMixin, TestCase):
    """Tests for New admin."""
    fixtures = ['dump.json']
    model = New
    object_id = 1
