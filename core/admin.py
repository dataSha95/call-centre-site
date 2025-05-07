from django.contrib import admin
from .models import ContactMessage,JobApplication,Service, BlogPost

admin.site.register(ContactMessage)
admin.site.register(JobApplication)
admin.site.register(Service)
admin.site.register(BlogPost)