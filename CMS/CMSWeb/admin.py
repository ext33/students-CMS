from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('FIO', 'email', 'group', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'group')
    fieldsets = (
        (None, {'fields': ('FIO', 'email', 'password', 'telephone', 'group', 'groups')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('FIO', 'email', 'password1', 'password2', 'telephone', 'group', 'is_active', 'is_staff', 'is_superuser', 'groups')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Groups)
class Groups(admin.ModelAdmin):
    list_display = ('group', 'direction')
    list_filter = ('course', 'direction')


@admin.register(Subject)
class Subjects(admin.ModelAdmin):
    list_display = ('subject', 'teacher')
    list_filter = ('teacher', 'course')


@admin.register(Performance)
class Perf(admin.ModelAdmin):
    list_display = ('FIO', 'subject', 'mark', 'date')
    list_filter = ('FIO', 'subject', 'mark', 'date', 'reporting_form')