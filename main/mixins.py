# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The mixins module from the main app."""

from django.contrib.contenttypes.models import ContentType
from django.views.generic.base import ContextMixin
from django_comments.models import Comment
from subjects.models import Subject

try:
    CONTENT_TYPE_SUBJECT = ContentType.objects.get_for_model(Subject)
except:
    CONTENT_TYPE_SUBJECT = None


class LastCommentsMixin(ContextMixin):
    """
    A mixin that adds the last five comment objects to the template context.

    Provides Comment objects in the variable 'last_comments'.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_comments'] = Comment.objects.filter(
            content_type=CONTENT_TYPE_SUBJECT).order_by('-submit_date')[:5]
        return context
