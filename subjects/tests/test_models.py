# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The test models from the subjects app."""


from django.test import TestCase
from ..models import Subject, Category


class CategoryModelTest(TestCase):
    """Tests for Category model."""

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name='Разработка программ',
            slug='develop',
            description='Описание',
            content='Содержание',
            price=5000,
            status=True
        )

    def test_get_absolute_url(self):
        category = Category.objects.get(slug='develop')
        self.assertEqual(category.get_absolute_url(), '/subjects/develop/')

    def test_is_enabled(self):
        category = Category.objects.get(slug='develop')
        self.assertTrue(category.is_enabled())


class SubjectModelTest(TestCase):
    """Tests for Subject model."""

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(
            name='Разработка программ',
            slug='develop',
            description='Описание',
            content='Содержание',
            price=5000,
            status=True
        )
        Subject.objects.create(
            name='Django site',
            description='Описание',
            content='Содердание',
            price=5000,
            status=Subject.STATUS_ENABLED,
            category=category
        )

    def test_get_absolute_url(self):
        subject = Subject.objects.get(pk=1)
        self.assertEqual(subject.get_absolute_url(), '/subjects/1/')

    def test_get_create_url(self):
        subject = Subject.objects.get(pk=1)
        self.assertEqual(subject.get_create_url(), '/orders/subject/1/')

    def test_get_status(self):
        subject = Subject.objects.get(pk=1)
        self.assertEqual(subject.status, Subject.STATUS_ENABLED)
        self.assertEqual(subject.get_status(), 'Доступно')

    def test_is_enabled(self):
        subject = Subject.objects.get(pk=1)
        self.assertTrue(subject.is_enabled())
