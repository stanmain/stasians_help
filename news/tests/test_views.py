# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test views module from the news app."""

from django.test import TestCase
from django.urls import reverse
from generic.tests import ViewTestMixin
from ..models import New


class NewsListViewTest(TestCase, ViewTestMixin):
    """Tests for NewsListView."""

    fixtures = ['dump.json']
    template = 'news/list.html'
    url_at_location = '/news/'
    url_by_name = reverse('news_list')

    def test_view_pagination(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('is_paginated', response.context)
        self.assertFalse(response.context['is_paginated'])

    def test_context_contains_news(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('object_list', response.context)
        news = New.objects.get(pk=1)
        self.assertIn(news, response.context['object_list'])


class NewsDetailViewTest(TestCase, ViewTestMixin):
    """Tests for NewsDetailView."""

    fixtures = ['dump.json']
    template = 'news/detail.html'
    url_at_location = '/news/1/'
    url_by_name = reverse('news_detail', kwargs={'slug': 1})

    def test_context_contains_new(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('object', response.context)
        new = New.objects.get(pk=1)
        self.assertEqual(new, response.context['object'])
