# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The models module from the subjects app."""

from django.db import models
from django.urls import reverse, reverse_lazy


class Category(models.Model):
    """Model category."""

    name = models.CharField(
        'Название',
        max_length=30,
        unique=True
    )
    slug = models.SlugField(
        'Slug',
        max_length=30,
        unique=True,
        db_index=True
    )
    description = models.TextField(
        'Описание',
        max_length=140
    )
    content = models.TextField(
        'Содержание'
    )
    price = models.SmallIntegerField(
        'Цена'
    )
    status = models.BooleanField(
        'Статус',
        default=True
    )

    class Meta:
        """Meta of category."""
        ordering = ('name',)
        unique_together = ('name', 'slug')
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '{} - {}'.format(self.name, self.description)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})

    def is_enabled(self):
        return self.status


class Subject(models.Model):
    """Model subject."""

    STATUS_DISABLED = 0
    STATUS_ENABLED = 1
    STATUS_EXPECTED = 2
    STATUS_CHOICES = (
        (STATUS_ENABLED, 'Доступно'),
        (STATUS_DISABLED, 'Недоступно'),
        (STATUS_EXPECTED, 'Ожидается'),
    )

    name = models.CharField(
        'Название',
        max_length=30,
        unique=True
    )
    description = models.TextField(
        'Описание',
        max_length=140
    )
    content = models.TextField(
        'Содержание'
    )
    price = models.SmallIntegerField(
        'Цена'
    )
    status = models.IntegerField(
        'Статус',
        choices=STATUS_CHOICES,
        default=STATUS_ENABLED
    )
    update = models.DateTimeField(
        'Дата обновления',
        db_index=True,
        auto_now=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        """Meta of category."""
        ordering = ('name',)
        unique_together = ('name',)
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subjects_detail', kwargs={'slug': self.id})

    def get_create_url(self):
        return reverse('order_create', kwargs={'slug': self.id})

    def get_status(self):
        for status in self.STATUS_CHOICES:
            if self.status == status[0]:
                return status[1]
        return None

    def is_enabled(self):
        if self.status is self.STATUS_ENABLED:
            return True
        return False
