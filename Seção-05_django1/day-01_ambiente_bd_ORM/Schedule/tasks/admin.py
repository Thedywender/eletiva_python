from django.contrib import admin
from tasks.models import Task


admin.site.site_header = "Everyday Tasks"
admin.site.register(Task)
