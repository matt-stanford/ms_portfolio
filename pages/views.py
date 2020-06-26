from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Job

def index(request):
    jobs = Job.objects.all()
    return render(request, 'pages/index.html', {'jobs': jobs})

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

        return redirect('index')
    return render(request, 'index.html', {})
