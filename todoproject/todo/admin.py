from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'completed', 'priority', 'created']
    list_filter = ['completed', 'priority', 'created']
    search_fields = ['title', 'description']
