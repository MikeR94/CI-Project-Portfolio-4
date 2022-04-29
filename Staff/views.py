from django.shortcuts import get_object_or_404, render
from Booking.models import Booking
from Reviews.models import Review
from Staff.forms import EditBookingForm, PaymentForm
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models import Sum
from datetime import date
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
        today = date.today()
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
            .filter(date_of_visit__lte=jan_end)
            .count()
        )
        feb_bookings = (
            Booking.objects.filter(date_of_visit__gte=feb_start)
            .filter(date_of_visit__lte=feb_end)
            .count()
        )
        mar_bookings = (
            Booking.objects.filter(date_of_visit__gte=mar_start)
            .filter(date_of_visit__lte=mar_end)
            .count()
        )
        apr_bookings = (
            Booking.objects.filter(date_of_visit__gte=apr_start)
            .filter(date_of_visit__lte=apr_end)
            .count()
        )
        may_bookings = (
            Booking.objects.filter(date_of_visit__gte=may_start)
            .filter(date_of_visit__lte=may_end)
            .count()
        )
        jun_bookings = (
            Booking.objects.filter(date_of_visit__gte=jun_start)
            .filter(date_of_visit__lte=jun_end)
            .count()
        )
        jul_bookings = (
            Booking.objects.filter(date_of_visit__gte=jul_start)
            .filter(date_of_visit__lte=jul_end)
            .count()
        )
        aug_bookings = (
            Booking.objects.filter(date_of_visit__gte=aug_start)
            .filter(date_of_visit__lte=aug_end)
            .count()
        )
        sep_bookings = (
            Booking.objects.filter(date_of_visit__gte=sep_start)
            .filter(date_of_visit__lte=sep_end)
            .count()
        )
        oct_bookings = (
            Booking.objects.filter(date_of_visit__gte=oct_start)
            .filter(date_of_visit__lte=oct_end)
            .count()
        )
        nov_bookings = (
            Booking.objects.filter(date_of_visit__gte=nov_start)
            .filter(date_of_visit__lte=nov_end)
            .count()
        )
        dec_bookings = (
            Booking.objects.filter(date_of_visit__gte=dec_start)
            .filter(date_of_visit__lte=dec_end)
            .count()
        )
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        pending_reviews = Review.objects.filter(acknowledged=False)
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
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
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
        }
        return render(request, "staff_dashboard.html", context)
    return render(request, "index.html")


def staff_pending_bookings(request):
    if request.user.is_staff:
        today = date.today()
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()

        context = {
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
        }
        return render(request, "staff_pending_bookings.html", context)


def staff_all_bookings(request):
    if request.user.is_staff:
        today = date.today()
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        all_bookings = Booking.objects.filter()
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
        context = {
            "all_bookings": all_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
        }
        return render(request, "staff_all_bookings.html", context)


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
        today = date.today()
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_reviews = Review.objects.filter(acknowledged=False)
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        pending_bookings = Booking.objects.filter(booking_acknowledged=False)
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
        context = {
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
        }
        return render(request, "staff_pending_reviews.html", context)


def staff_all_reviews(request):
    if request.user.is_staff:
        today = date.today()
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        all_reviews = Review.objects.filter()
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
        context = {
            "all_reviews": all_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
        }
        return render(request, "staff_all_reviews.html", context)


def staff_check_in_page(request):
    if request.user.is_staff:
        today = date.today()
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_bookings_count = Booking.objects.filter(
            booking_acknowledged=False
        ).count()
        pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
        guest_attended = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        )
        context = {
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
            "guest_attended": guest_attended,
        }
        return render(request, "staff_check_in.html", context)


def staff_check_in(request, booking_id):
    next = request.POST.get("next", "/")
    data = Booking.objects.filter(id=booking_id)
    for item in data:
        item.guest_attended = True
        item.save()
        return HttpResponseRedirect(next)


def staff_no_show(request, booking_id):
    next = request.POST.get("next", "/")
    data = Booking.objects.filter(id=booking_id)
    for item in data:
        item.guest_no_show = True
        item.save()
        return HttpResponseRedirect(next)


def staff_approve_review(request, review_id):
    next = request.POST.get("next", "/")
    data = Review.objects.filter(id=review_id)
    for item in data:
        item.approved = True
        item.acknowledged = True
        item.save()
        return HttpResponseRedirect(next)


def staff_deny_review(request, review_id):
    next = request.POST.get("next", "/")
    data = Review.objects.filter(id=review_id)
    for item in data:
        item.approved = False
        item.acknowledged = True
        item.save()
        return HttpResponseRedirect(next)


def staff_details_booking(request, booking_id):
    today = date.today()
    next = request.POST.get("next", "/")
    booking_data = get_object_or_404(Booking, id=booking_id)
    booking = Booking.objects.get(id=booking_id)
    pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
    pending_bookings = Booking.objects.filter(booking_acknowledged=False)
    pending_reviews_count = Review.objects.filter(acknowledged=False).count()
    pending_reviews = Review.objects.filter(acknowledged=False)
    pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
    if request.method == "POST":
        form = EditBookingForm(request.POST, instance=booking_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(next)
    form = EditBookingForm(instance=booking_data)
    context = {
        "booking": booking,
        "form": form,
        "pending_bookings": pending_bookings,
        "pending_bookings_count": pending_bookings_count,
        "pending_reviews": pending_reviews,
        "pending_reviews_count": pending_reviews_count,
        "pending_check_in_count": pending_check_in_count,
    }
    return render(request, "staff_details_booking.html", context)


def staff_payment_page(request):
    today = date.today()
    booking = Booking.objects.filter(guest_attended=True, bill_settled=False)
    pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
    pending_bookings = Booking.objects.filter(booking_acknowledged=False)
    pending_reviews_count = Review.objects.filter(acknowledged=False).count()
    pending_reviews = Review.objects.filter(acknowledged=False)
    pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
    context = {
        "booking": booking,
        "pending_bookings": pending_bookings,
        "pending_bookings_count": pending_bookings_count,
        "pending_reviews": pending_reviews,
        "pending_reviews_count": pending_reviews_count,
        "pending_check_in_count": pending_check_in_count,
    }
    return render(request, "staff_payment_page.html", context)


def staff_create_payment(request, booking_id):
    today = date.today()
    next = request.POST.get("next", "/")
    booking = get_object_or_404(Booking, id=booking_id)
    data = Booking.objects.filter(id=booking_id)
    form = PaymentForm()
    pending_bookings_count = Booking.objects.filter(booking_acknowledged=False).count()
    pending_bookings = Booking.objects.filter(booking_acknowledged=False)
    pending_reviews_count = Review.objects.filter(acknowledged=False).count()
    pending_reviews = Review.objects.filter(acknowledged=False)
    pending_check_in_count = Booking.objects.filter(
            guest_attended=False,
            guest_no_show=False,
            booking_approved=True,
            date_of_visit__year=today.year,
            date_of_visit__month=today.month,
            date_of_visit__day=today.day,
        ).count()
    pending_payment_count = Booking.objects.filter(guest_attended=True, bill_settled=False).count()
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.booking_id = booking_id
            form.amount_tipped = int(form.amount_paid) - int(form.amount_owed)
            form.total_income = int(form.amount_paid) + int(form.amount_tipped)
            if int(form.amount_paid) < int(form.amount_owed):
                form.amount_tipped = 0
            for x in data:
                if int(form.amount_owed) <= int(form.total_income):
                    x.bill_settled = True
                    x.save()
            form.save()
            return HttpResponseRedirect(next)
    context = {
        "booking": booking,
        "form": form,
        "pending_bookings": pending_bookings,
        "pending_bookings_count": pending_bookings_count,
        "pending_reviews": pending_reviews,
        "pending_reviews_count": pending_reviews_count,
        "pending_check_in_count": pending_check_in_count,
        "pending_payment_count": pending_payment_count,
    }
    return render(request, "staff_submit_payment.html", context)
