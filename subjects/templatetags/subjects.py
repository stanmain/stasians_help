# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The templatetags-subjects module from the subjects app."""

from django import template

from ..models import Category, Subject


register = template.Library()


@register.inclusion_tag('subjects/sidebar/category.html')
def render_category_sidebar():
    categories = Category.objects.filter(status=True).exclude(slug='other')
    try:
        other = Category.objects.get(slug='other')
    except Category.DoesNotExist:
        other = None
    return {
        'categories': categories,
        'other_category': other,
    }


@register.inclusion_tag('subjects/sidebar/expected.html')
def render_expected_sidebar():
    subjects = Subject.objects.filter(
        status=Subject.STATUS_EXPECTED
    ).order_by(
        'update'
    )[0:3]
    return {
        'expected_subjects': subjects,
    }
