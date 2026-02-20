from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse
from base.models import Contact
from base import models
# Create your views here.
def home(request):
    if request.method == 'POST':
        print("POST request received")
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        phone = request.POST.get('phone', '')
        print(name, email, message, phone)
        
        if len(name) < 2 or len(email) < 2 or len(message) < 2 or len(phone) < 2:
            messages.error(request, "Please enter correct information")
        else:
            contact_instance = Contact(name=name, email=email, message=message, phone=phone)
            contact_instance.save()
            messages.success(request, "Thank You For Contacting Me!!")
    return render(request, 'home.html')