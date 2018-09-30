# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The models module from the news app."""


from django.db import models
from django.urls import reverse


class New(models.Model):
    """Model of news."""

    title = models.CharField(
        'Заголовок',
        max_length=140,
        unique_for_date='update'
    )
    description = models.TextField(
        'Описание',
        max_length=140
    )
    content = models.TextField(
        'Содержание'
    )
    pubdate = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    update = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )
    status = models.BooleanField(
        'Статус',
        default=True
    )

    class Meta:
        ordering = ['-pubdate']
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return '{} - {}'.format(self.title, self.description)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.pk})
