# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the news app."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import New


class NewsListView(ListView):
    """A view for displaying news list."""
    model = New
    template_name = 'news/list.html'
    paginate_by = 10


class NewsDetailView(DetailView):
    """A view for displaying news detail."""
    model = New
    template_name = 'news/detail.html'
    slug_field = 'pk'
