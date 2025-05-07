from django.shortcuts import render,redirect
from .forms import ContactForm

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
