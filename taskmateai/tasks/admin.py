from django.contrib import admin

from tasks.models import Tasks, AIResponse

# Register your models here.
admin.site.register(Tasks)
admin.site.register(AIResponse)