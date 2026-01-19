from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import userreg
import random
from django.core.mail import send_mail

def home(request):
    return render(request, "master.html")

def members(request):
    myusers = userreg.objects.all().values()
    context = {
        'user_members' : myusers,
    }
    return render(request, "login.html", context)

def details(request, slug):
    mymembers = userreg.objects.get(slug = slug)
    context = {
        "member" : mymembers,
    }
    return render(request, "detail.html", context)

@require_POST
def send_test_email(request, slug):
    person = get_object_or_404(userreg, slug=slug)
    otp = random.randint(100000,999999)
    email_subject = "Just Review this Mail"
    email_message = (
        f"Hello {person.name},\n\n"
        f"Welcome to the Django Project!\n\n"
        f"Here are your details:\n"
        f"Email: {person.email}\n"
        f"OTP Key: {otp}\n\n"
        f"Best Regards,\nVenkat"
    )
    try:
        send_mail(
            email_subject,
            email_message,
            None,
            [person.email],
            fail_silently=False,
        )
        messages.success(request, "Email sent successfully!")
        # return HttpResponse("Email Sent!")
    except Exception as e:
        messages.error(request, f"Failed to send Email! {str(e)}")
        # return HttpResponse(e)
    return redirect('details', slug=slug)
    