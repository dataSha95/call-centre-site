from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Service, BlogPost


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    
def about(request):
    return render(request, 'about.html')

from .forms import JobApplicationForm

def apply_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
    else:
        form = JobApplicationForm()
    return render(request, 'apply_job.html', {'form': form})
    
def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services': all_services})


def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})