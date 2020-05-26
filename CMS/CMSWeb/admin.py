from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'email', 'telephone', 'FIO', 'group', 'is_active', 'is_staff', 'is_superuser')
    list_display = ('username', 'FIO', 'group')
    list_filter = ('group', 'is_staff', 'is_active')


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