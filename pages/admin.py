from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'github_url', 'upload_date')
    
admin.site.register(Job, JobAdmin)
