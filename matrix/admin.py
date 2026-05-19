from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "quadrant", "is_completed", "due_date", "created_at")
    list_filter = ("quadrant", "is_completed")
    search_fields = ("title", "description")
