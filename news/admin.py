# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The admin module from the news app."""

from django.contrib import admin

from .models import New


admin.site.register(New)
