# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test mixin module from the tests app."""

from django.test import TestCase
from ..models import New
from ..mixins import LatestNewsMixin


class LatestNewsMixinTest(TestCase):
    """Tests for LatestNewsMixin."""

    fixtures = ['dump.json']

    def test_context_contains_last_news(self):
        context = LatestNewsMixin().get_context_data()
        self.assertIn('news', context)
        new = New.objects.get(pk=1)
        self.assertIn(new, context['news'])
