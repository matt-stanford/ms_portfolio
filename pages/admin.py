from django.contrib import admin
from .models import Job, Course

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'github_url', 'url', 'upload_date')
    list_display_links = ('id', 'title')
    
admin.site.register(Job, JobAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'upload_date')
    list_display_links = ('id', 'title')
    
admin.site.register(Course, CourseAdmin)
