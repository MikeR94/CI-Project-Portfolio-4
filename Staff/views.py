from django.shortcuts import render
from Booking.models import Booking
from Reviews.models import Review
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import Sum
from Staff.utils import (
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

def staff_dashboard(request):
    if request.user.is_staff:
        jan_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jan_start)
            .filter(date_of_visit__lte=jan_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        feb_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=feb_start)
            .filter(date_of_visit__lte=feb_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        mar_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=mar_start)
            .filter(date_of_visit__lte=mar_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        apr_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=apr_start)
            .filter(date_of_visit__lte=apr_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        may_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=may_start)
            .filter(date_of_visit__lte=may_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        jun_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jun_start)
            .filter(date_of_visit__lte=jun_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        jul_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=jul_start)
            .filter(date_of_visit__lte=jul_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        aug_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=aug_start)
            .filter(date_of_visit__lte=aug_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        sep_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=sep_start)
            .filter(date_of_visit__lte=sep_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        oct_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=oct_start)
            .filter(date_of_visit__lte=oct_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        nov_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=nov_start)
            .filter(date_of_visit__lte=nov_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        dec_guests = (
            Booking.objects.filter(guest_attended=True)
            .filter(date_of_visit__gte=dec_start)
            .filter(date_of_visit__lte=dec_end)
            .aggregate(sum=Sum("number_of_guests"))["sum"]
        )
        jan_bookings = (
            Booking.objects.filter(date_of_visit__gte=jan_start)
            .filter(date_of_visit__lte=jan_end).count()
        )
        feb_bookings = (
            Booking.objects.filter(date_of_visit__gte=feb_start)
            .filter(date_of_visit__lte=feb_end).count()
        )
        mar_bookings = (
            Booking.objects.filter(date_of_visit__gte=mar_start)
            .filter(date_of_visit__lte=mar_end).count()
        )
        apr_bookings = (
            Booking.objects.filter(date_of_visit__gte=apr_start)
            .filter(date_of_visit__lte=apr_end).count()
        )
        may_bookings = (
            Booking.objects.filter(date_of_visit__gte=may_start)
            .filter(date_of_visit__lte=may_end).count()
        )
        jun_bookings = (
            Booking.objects.filter(date_of_visit__gte=jun_start)
            .filter(date_of_visit__lte=jun_end).count()
        )
        jul_bookings = (
            Booking.objects.filter(date_of_visit__gte=jul_start)
            .filter(date_of_visit__lte=jul_end).count()
        )
        aug_bookings = (
            Booking.objects.filter(date_of_visit__gte=aug_start)
            .filter(date_of_visit__lte=aug_end).count()
        )
        sep_bookings = (
            Booking.objects.filter(date_of_visit__gte=sep_start)
            .filter(date_of_visit__lte=sep_end).count()
        )
        oct_bookings = (
            Booking.objects.filter(date_of_visit__gte=oct_start)
            .filter(date_of_visit__lte=oct_end).count()
        )
        nov_bookings = (
            Booking.objects.filter(date_of_visit__gte=nov_start)
            .filter(date_of_visit__lte=nov_end).count()
        )
        dec_bookings = (
            Booking.objects.filter(date_of_visit__gte=dec_start)
            .filter(date_of_visit__lte=dec_end).count()
        )
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
        pending_reviews = Review.objects.filter(approved=False)
        pending_reviews_count = Review.objects.filter(approved=False).count()
        context = {
            "jan_guests": jan_guests,
            "feb_guests": feb_guests,
            "mar_guests": mar_guests,
            "apr_guests": apr_guests,
            "may_guests": may_guests,
            "jun_guests": jun_guests,
            "jul_guests": jul_guests,
            "aug_guests": aug_guests,
            "sep_guests": sep_guests,
            "oct_guests": oct_guests,
            "nov_guests": nov_guests,
            "dec_guests": dec_guests,
            "jan_bookings": jan_bookings,
            "feb_bookings": feb_bookings,
            "mar_bookings": mar_bookings,
            "apr_bookings": apr_bookings,
            "may_bookings": may_bookings,
            "jun_bookings": jun_bookings,
            "jul_bookings": jul_bookings,
            "aug_bookings": aug_bookings,
            "sep_bookings": sep_bookings,
            "oct_bookings": oct_bookings,
            "nov_bookings": nov_bookings,
            "dec_bookings": dec_bookings,
            'pending_bookings': pending_bookings,
            'pending_bookings_count': pending_bookings_count,
            'pending_reviews': pending_reviews,
            'pending_reviews_count': pending_reviews_count,
        }
        return render(request, "staff_dashboard.html", context)
    return render(request, "index.html")


def staff_pending_bookings(request):
    if request.user.is_staff:
        pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        pending_reviews_count = Review.objects.filter(approved=False).count()
        pending_reviews = Review.objects.filter(approved=False)
        context = {
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
        }
        return render(request, "staff_pending_bookings.html", context)


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


def staff_pending_reviews(request):
    if request.user.is_staff:
        pending_reviews_count = Review.objects.filter(approved=False).count()
        pending_reviews = Review.objects.filter(approved=False)
        pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        context = {
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
        }
        return render(request, "staff_pending_reviews.html", context)


def approve_review(request, review_id):
    next = request.POST.get("next", "/")
    data = Review.objects.filter(id=review_id)
    for item in data:
        item.approved = True
        item.acknowledged = True
        item.save()
        return HttpResponseRedirect(next)


def deny_review(request, review_id):
    next = request.POST.get("next", "/")
    data = Review.objects.filter(id=review_id)
    for item in data:
        item.approved = False
        item.acknowledged = True
        item.save()
        return HttpResponseRedirect(next)