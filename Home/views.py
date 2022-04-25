from django.shortcuts import render
from Booking.models import Booking
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import datetime as dt
from django.db.models import Sum
from Home.utils import (
    jan_start,
    jan_end,
    feb_start,
    feb_end,
    mar_start,
    mar_end,
    apr_start,
    apr_end,
    may_start,
    may_end,
    jun_start,
    jun_end,
    jul_start,
    jul_end,
    aug_start,
    aug_end,
    sep_start,
    sep_end,
    oct_start,
    oct_end,
    nov_start,
    nov_end,
    dec_start,
    dec_end,
)

# Create your views here.


def index(request):
    return render(request, "index.html")


def staff_dashboard(request):
    if request.user.is_staff:
        jan_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jan_start)
            .filter(date_of_visit__lte=jan_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        feb_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=feb_start)
            .filter(date_of_visit__lte=feb_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        mar_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=mar_start)
            .filter(date_of_visit__lte=mar_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        apr_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=apr_start)
            .filter(date_of_visit__lte=apr_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        may_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=may_start)
            .filter(date_of_visit__lte=may_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        jun_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jun_start)
            .filter(date_of_visit__lte=jun_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        jul_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jul_start)
            .filter(date_of_visit__lte=jul_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        aug_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=aug_start)
            .filter(date_of_visit__lte=aug_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        sep_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=sep_start)
            .filter(date_of_visit__lte=sep_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        oct_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=oct_start)
            .filter(date_of_visit__lte=oct_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        nov_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=nov_start)
            .filter(date_of_visit__lte=nov_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        dec_count = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=dec_start)
            .filter(date_of_visit__lte=dec_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        context = {
            "jan_count": jan_count,
            "feb_count": feb_count,
            "mar_count": mar_count,
            "apr_count": apr_count,
            "may_count": may_count,
            "jun_count": jun_count,
            "jul_count": jul_count,
            "aug_count": aug_count,
            "sep_count": sep_count,
            "oct_count": oct_count,
            "nov_count": nov_count,
            "dec_count": dec_count,
        }
        return render(request, "staff/staff-dashboard.html", context)
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
    template = render_to_string("approved_email_template.html")
    email = EmailMessage(
        "Cafe Manbo - [BOOKING APPROVED]",
        template,
        settings.EMAIL_HOST_USER,
        ["mikeyralph@hotmail.co.uk"],
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
    template = render_to_string("denied_email_template.html")
    email = EmailMessage(
        "Cafe Manbo - [BOOKING DENIED]",
        template,
        settings.EMAIL_HOST_USER,
        ["mikeyralph@hotmail.co.uk"],
    )
    email.fail_silently = False
    email.send()
    for object in booking:
        object.booking_denied = True
        object.booking_acknowledged = True
        object.save()
    return HttpResponseRedirect(next)
