from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Job, Course
import os

def index(request):
    jobs = Job.objects.all().order_by('-upload_date')
    return render(request, 'pages/index.html', {'jobs': jobs})

def my_courses(request):
    courses = Course.objects.all().order_by('-upload_date')
    return render(request, 'pages/my_courses.html', {'courses': courses})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
            f'Email from {name}',
            message,
            email,
            ['mjfstanford@gmail.com',]
        )
        messages.success(request, f'Thanks for your message, {name}. I\'ll be in touch soon!')
        return redirect('index')
    return render(request, 'index.html', {})
