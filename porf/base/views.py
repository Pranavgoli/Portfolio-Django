from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse
from base.models import Contact
from base import models
from django.core.mail import send_mail
from django.conf import settings
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
            
            # Send Email Notification to yourself
            try:
                subject = f"New Portfolio Contact from {name}"
                body = f"You received a new message from your portfolio website!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
                
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],  # This sends the email to the same address used to authenticate
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")
                
            messages.success(request, "Thank You For Contacting Me!!")
    return render(request, 'home.html')