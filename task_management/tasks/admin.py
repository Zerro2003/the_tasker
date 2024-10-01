from django.contrib import admin
from .models import User, Task

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'is_complete', 'priority_level')

admin.site.register(User)
