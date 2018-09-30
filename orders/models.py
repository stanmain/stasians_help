# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The models module from the orders app."""

from django.conf import settings
from django.db import models
from django.urls import reverse

from subjects.models import Subject


class Order(models.Model):
    """Model of order."""

    STATUS_NEW = 0
    STATUS_PREPAYMENT = 1
    STATUS_DO = 2
    STATUS_PAYMENT = 3
    STATUS_COMPLETED = 4
    STATUS_CANCELED = 5
    STATUS_DISAPPROVED = 6
    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_PREPAYMENT, 'Ожидает предоплаты'),
        (STATUS_DO, 'Выполняется'),
        (STATUS_PAYMENT, 'Ожидает оплаты'),
        (STATUS_COMPLETED, 'Завершён'),
        (STATUS_CANCELED, 'Отменён'),
        (STATUS_DISAPPROVED, 'Отклонено')
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,
        verbose_name='Предмет',
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        null=True
    )
    description = models.TextField(
        'Описание'
    )
    solution = models.TextField(
        'Решение',
        null=True,
        blank=True
    )
    pubdate = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    update = models.DateTimeField(
        'Дата обновления',
        auto_now=True
    )
    status = models.PositiveSmallIntegerField(
        'Статус',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    price = models.PositiveIntegerField(
        'Стоимость',
        default=0
    )

    class Meta:
        ordering = ('update', 'pubdate')
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ #{}'.format(self.id)

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'slug': self.id})

    def get_slug(self):
        return self.id

    def get_status(self):
        for status in self.STATUS_CHOICES:
            if self.status == status[0]:
                return status[1]
        return None

    def paid(self):
        x = self.statement_set.aggregate(models.Sum('amount'))['amount__sum']
        if x is None:
            return 0
        return x

    def prepayment(self):
        paid = self.paid()
        prepayment = self.price * 0.25
        if self.price and paid >= prepayment:
            return 'Внесено'
        return prepayment - paid

    def payment(self):
        paid = self.paid()
        if self.price and paid >= self.price:
            return 'Оплачено'
        return self.price - paid

    paid.short_description = 'Внесено'
    payment.short_description = 'к оплате'
    prepayment.short_description = 'предоплата'

    def can_canceled(self):
        if self.status in (self.STATUS_COMPLETED, self.STATUS_CANCELED,
                           self.STATUS_DISAPPROVED):
            return False
        return True

    def cancel(self):
        self.status = self.STATUS_CANCELED


class Statement(models.Model):
    """Model of statement."""

    date = models.DateTimeField(
        'Дата'
    )
    amount = models.PositiveIntegerField(
        'Сумма'
    )
    terminal = models.TextField(
        'Терминал'
    )
    description = models.TextField(
        'Описание'
    )
    order = models.ForeignKey(
        Order,
        models.SET_NULL,
        verbose_name='Заказ',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'Выписка'
        verbose_name_plural = 'Выписки'

    def __str__(self):
        return 'Выписка #{}'.format(self.id)
