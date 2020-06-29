from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    technology = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    upload_date = models.DateTimeField(default=datetime.now)

    @property
    def short_summary(self):
        return f'{self.summary[:100]}...'

    def __str__(self):
        return self.title

    objects = models.Manager()

