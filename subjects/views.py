# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The views module from the subjects app."""

from django.http import Http404
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView

from .models import Subject, Category


class SubjectListView(ListView):
    """View of subjects list."""

    queryset = Subject.objects.filter(status=Subject.STATUS_ENABLED)
    template_name = 'subjects/list.html'
    paginate_by = 10
    context_object_name = 'subjects'


class SubjectDetailView(DetailView):
    """View of subject detail."""
    model = Subject
    template_name = 'subjects/detail.html'
    slug_field = 'pk'

    def get_object(self, queryset=None):
        subject = super().get_object(queryset)
        if subject.status is not Subject.STATUS_ENABLED:
            raise Http404
        return subject


class CategoryView(ListView, SingleObjectMixin):
    """View of category detail that contains subjects list."""

    template_name = 'subjects/category.html'
    paginate_by = 10
    context_object_name = 'subjects'

    def get(self, request, *args, **kwargs):
        self.object = Category.objects.get(slug=self.kwargs['slug'])
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return Subject.objects.filter(
            category=self.object,
            status=Subject.STATUS_ENABLED
        ).order_by('name')
