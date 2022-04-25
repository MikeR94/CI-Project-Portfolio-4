from django.shortcuts import render
from Booking.models import Booking
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, "index.html")


def staff_dashboard(request):
    if request.user.is_staff:
        return render(request, "staff/staff-dashboard.html")
    return render(request, "index.html")


def staff_pending_bookings(request):
    if request.user.is_staff:
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        context = {
            "pending_bookings": pending_bookings,
        }
        return render(request, "staff/staff-pending-bookings.html", context)


def staff_approve_booking(request, booking_id):
    next = request.POST.get("next", "/")
    booking = Booking.objects.filter(id=booking_id)
    template = render_to_string('approved_email_template.html')
    email = EmailMessage(
        'Cafe Manbo - [BOOKING APPROVED]',
        template,
        settings.EMAIL_HOST_USER,
        ['mikeyralph@hotmail.co.uk'],
    )
    email.fail_silently = False
    email.send()
    for object in booking:
        object.booking_approved = True
        object.booking_acknowledged = True
        object.save()
    return HttpResponseRedirect(next)


def staff_deny_booking(request, booking_id):
    next = request.POST.get("next", "/")
    booking = Booking.objects.filter(id=booking_id)
    template = render_to_string('denied_email_template.html')
    email = EmailMessage(
        'Cafe Manbo - [BOOKING DENIED]',
        template,
        settings.EMAIL_HOST_USER,
        ['mikeyralph@hotmail.co.uk'],
    )
    email.fail_silently = False
    email.send()
    for object in booking:
        object.booking_denied = True
        object.booking_acknowledged = True
        object.save()
    return HttpResponseRedirect(next)