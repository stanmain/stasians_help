# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The tests module from the main app."""

from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse
from django_comments.models import Comment
from generic.tests import ViewTestMixin
from news.models import New
from subjects.models import Subject
from .mixins import LastCommentsMixin


class MainPageViewTest(TestCase, ViewTestMixin):
    """Tests for MainPageView."""

    fixtures = ['dump.json']
    template = 'main/index.html'
    url_at_location = '/'
    url_by_name = reverse('index')

    def test_context_contains_popular_subjects(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('popular_subjects', response.context)
        python = Subject.objects.get(pk=1)
        self.assertIn(python, response.context['popular_subjects'])
        cpp = Subject.objects.get(pk=2)
        self.assertIn(cpp, response.context['popular_subjects'])
        arduino = Subject.objects.get(pk=3)
        self.assertNotIn(arduino, response.context['popular_subjects'])

    def test_context_contains_latest_news(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('news', response.context)
        news = New.objects.order_by('-pubdate')[:5]
        for new in news:
            self.assertIn(new, response.context['news'])

    def test_context_contains_latest_comments(self):
        response = self.client.get(self.url_by_name)
        self.assertIn('last_comments', response.context)
        CONTENT_TYPE_SUBJECT = ContentType.objects.get_for_model(Subject)
        comments = Comment.objects.filter(
            content_type=CONTENT_TYPE_SUBJECT).order_by('-submit_date')[:5]
        for comment in comments:
            self.assertIn(comment, response.context['last_comments'])


class LastCommentsMixinTest(TestCase):
    """Tests for LastCommentsMixin."""
    fixtures = ['dump.json']

    def test_context_contains_latest_comments(self):
        context = LastCommentsMixin().get_context_data()
        self.assertIn('last_comments', context)
        CONTENT_TYPE_SUBJECT = ContentType.objects.get_for_model(Subject)
        comments = Comment.objects.filter(
            content_type=CONTENT_TYPE_SUBJECT).order_by('-submit_date')[:5]
        for comment in comments:
            self.assertIn(comment, context['last_comments'])
