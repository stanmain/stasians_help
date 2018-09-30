# Copyright © 2018 Stanislav Hnatiuk. All rights reserved.

"""The admin module from the profiles app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from .models import Profile, ExUser, ExGroup


class ExGroupAdmin(GroupAdmin):
    list_display = ('name',)


admin.site.unregister(Group)
admin.site.register(ExGroup, ExGroupAdmin)


class ProfileInline(admin.StackedInline):
    """"""

    model = Profile
    can_delete = False
    verbose_name = 'Профиль'
    verbose_name_plural = 'Дополнительная информация'


@admin.register(ExUser)
class ExUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Персональная информация', {
            'fields': ('email',)
        }),
        ('Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    inlines = (ProfileInline,)
