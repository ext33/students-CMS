from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ('email', 'FIO', 'group', 'telephone')
    list_filter = ('FIO', 'group')


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