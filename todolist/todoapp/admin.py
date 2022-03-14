from django.contrib import admin
from .models import todolist


@admin.register(todolist)
class todolistAdmin(admin.ModelAdmin):
    list_display = ['project', 'active', 'description', 'user']
