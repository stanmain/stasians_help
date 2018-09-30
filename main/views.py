# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the main app."""

from django.views.generic.base import TemplateView

from news.mixins import LatestNewsMixin
from subjects.mixins import PopularSubjectMixin
from .mixins import LastCommentsMixin


class MainPageView(LatestNewsMixin, PopularSubjectMixin, LastCommentsMixin,
                   TemplateView):
    """View for displaying main (index) page."""

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['caption'] = 'Обзор'
        return context
