from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def book_now(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            instance.save()
            context = {
            "data": instance,
        }
        template = render_to_string('email_template.html')
        email = EmailMessage(
            'Thank you for booking!',
            template,
            settings.EMAIL_HOST_USER,
            ['mikeyralph@hotmail.co.uk'],
        )
        email.fail_silently = False
        email.send()
        return render(request, "book-success.html", context)
    form = forms.BookingForm()
    context = {
        "form": form,
        }
    return render(request, "book-now.html", context)
