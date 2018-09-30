# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test admin from the orders app."""

from django.test import TestCase
from generic.tests import AdminTestMixin
from ..models import Order


class OrderAdminTest(AdminTestMixin, TestCase):
    """Tests for Order admin."""

    fixtures = ['dump.json']
    model = Order
    object_id = 1
