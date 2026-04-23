from django.contrib import admin
from .models import Plant, Note, Task


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'plant_type', 'location', 'is_healthy', 'last_watered', 'created_at']
    list_filter = ['plant_type', 'is_healthy', 'light_need']
    search_fields = ['name', 'species', 'user__username']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['plant', 'created_at', 'updated_at']
    search_fields = ['content', 'plant__name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['plant', 'task_type', 'due_date', 'completed']
    list_filter = ['task_type', 'completed']
    search_fields = ['plant__name']
