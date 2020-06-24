from django.shortcuts import render
from .models import Job

def index(request):
    jobs = Job.objects.all()
    return render(request, 'pages/index.html', {'jobs': jobs})
