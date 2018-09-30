# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The main templatetags module from the main app."""

from django import template


register = template.Library()


@register.inclusion_tag('sidebar.html')
def render_sidebar():
    return {}
