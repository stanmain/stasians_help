# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The models module from the profiles app."""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager, Group)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.validators import EmailValidator
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ExUser(AbstractBaseUser, PermissionsMixin):
    """
    A custom model that extends the basic user model.

    Username, password and email are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters and digits only.'
        ),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        validators=[email_validator],
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return self.profile.get_full_name()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.profile.get_short_name()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ExGroup(Group):
    """A custom group model that move model in current app."""
    class Meta:
        verbose_name = _('группа')
        verbose_name_plural = _('группы')


class Profile(models.Model):
    """User profile."""

    first_name = models.CharField(
        'Имя',
        max_length=140,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=140,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        'Биография',
        max_length=1024,
        blank=True
    )
    location = models.CharField(
        'Место положения',
        max_length=140,
        blank=True
    )
    birth_date = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles', kwargs={'slug': self.user.username})

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


@receiver(post_save, sender=ExUser)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
