from django.shortcuts import get_object_or_404, render, redirect
from Booking.models import Booking
from Reviews.models import Review
from Staff.models import Payment
from Accounts.models import User
from django.utils import timezone
from . import forms
from Booking.forms import BookingForm
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
        standard_income = (
            Payment.objects.filter().aggregate(sum=Sum("amount_paid"))["sum"]
        )
        amount_tipped = (
            Payment.objects.filter().aggregate(sum=Sum("amount_tipped"))["sum"]
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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        booking_count = Booking.objects.all().count()
        income_count = Payment.objects.all().aggregate(Sum('total_income')).get('total_income__sum', 0.00)
        total_guests = Booking.objects.filter(guest_attended=True).aggregate(sum=Sum('number_of_guests'))['sum']
        review_count = Review.objects.all().count()
        staff_accounts = User.objects.filter(is_staff=True).count()
        user_accounts = User.objects.filter(is_staff=False).count()
        all_accounts = User.objects.all().count()
        reviews_approved = Review.objects.filter(approved=True, acknowledged=True).count()
        reviews_denied = Review.objects.filter(approved=False, acknowledged=True).count()
        try:
            average_per_guest =  int(0 if income_count is None else income_count) / int(0 if total_guests is None else total_guests)
        except ZeroDivisionError:
            average_per_guest = 50
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
            "standard_income": standard_income,
            "amount_tipped": amount_tipped,
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
            "booking_count": booking_count,
            "income_count": income_count,
            "total_guests": total_guests,
            "review_count": review_count,
            "staff_accounts": staff_accounts,
            "user_accounts": user_accounts,
            "all_accounts": all_accounts,
            "reviews_approved": reviews_approved,
            "reviews_denied": reviews_denied,
            "average_per_guest": average_per_guest

        }
        return render(request, "staff_dashboard.html", context)
    else:
        return HttpResponseRedirect("/")


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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()

        context = {
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_pending_bookings.html", context)
    else:
        return HttpResponseRedirect("/")


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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        context = {
            "all_bookings": all_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_all_bookings.html", context)
    else:
        return HttpResponseRedirect("/")


def staff_approve_booking(request, booking_id):
    if request.user.is_staff:
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
    else:
        return HttpResponseRedirect("/")


def staff_deny_booking(request, booking_id):
    if request.user.is_staff:
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
    else:
        return HttpResponseRedirect("/")


def staff_cancel_booking(request, booking_id):
    if request.user.is_staff:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect("staff_dashboard")
    else:
        return HttpResponseRedirect("/")



def staff_pending_reviews(request):
    if request.user.is_staff:
        today = date.today()
        pending_reviews_count = Review.objects.filter(acknowledged=False).count()
        pending_reviews = Review.objects.filter(acknowledged=False)
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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        context = {
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_pending_reviews.html", context)
    else:
        return HttpResponseRedirect("/")


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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        context = {
            "all_reviews": all_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_all_reviews.html", context)
    else:
        return HttpResponseRedirect("/")


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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        for booking in Booking.objects.filter(no_show_email_sent=False):
            if booking.date_of_visit < timezone.now().date():
                booking.no_show_email_sent = True
                template = render_to_string("no_show_email_template.html")
                email = EmailMessage(
                    "Cafe Manbo - [NO SHOW]",
                    template,
                    settings.EMAIL_HOST_USER,
                    ["mikeyralph@hotmail.co.uk"],
                )
                email.fail_silently = False
                email.send()
                booking.save()

        context = {
            "pending_reviews_count": pending_reviews_count,
            "pending_bookings_count": pending_bookings_count,
            "pending_check_in_count": pending_check_in_count,
            "guest_attended": guest_attended,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_check_in.html", context)
    else:
        return HttpResponseRedirect("/")


def staff_check_in(request, booking_id):
    if request.user.is_staff:
        next = request.POST.get("next", "/")
        data = Booking.objects.filter(id=booking_id)
        template = render_to_string("checked_in_email_template.html")
        email = EmailMessage(
            "Cafe Manbo - [CHECKED IN]",
            template,
            settings.EMAIL_HOST_USER,
            ["mikeyralph@hotmail.co.uk"],
        )
        email.fail_silently = False
        email.send()
        for item in data:
            item.guest_attended = True
            item.save()
            return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect("/")


def staff_no_show(request, booking_id):
    if request.user.is_staff:
        next = request.POST.get("next", "/")
        data = Booking.objects.filter(id=booking_id)
        for item in data:
            item.guest_no_show = True
            item.save()
            return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect("/")


def staff_approve_review(request, review_id):
    if request.user.is_staff:
        next = request.POST.get("next", "/")
        data = Review.objects.filter(id=review_id)
        for item in data:
            item.approved = True
            item.acknowledged = True
            item.save()
            return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect("/")


def staff_deny_review(request, review_id):
    if request.user.is_staff:
        next = request.POST.get("next", "/")
        data = Review.objects.filter(id=review_id)
        for item in data:
            item.approved = False
            item.acknowledged = True
            item.save()
            return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect("/")


def staff_details_booking(request, booking_id):
    if request.user.is_staff:
        today = date.today()
        next = request.POST.get("next", "/")
        booking_data = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST or None, instance=booking_data)
        print(form)
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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
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
    else:
        return HttpResponseRedirect("accounts_login")
    if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(next)
    return render(request, "staff_details_booking.html", context)


def staff_payment_page(request):
    if request.user.is_staff:
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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        context = {
            "booking": booking,
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
        return render(request, "staff_payment_page.html", context)
    else:
        return HttpResponseRedirect("/")


def staff_create_payment(request, booking_id):
    if request.user.is_staff:
        today = date.today()
        form = forms.PaymentForm(request.POST or None)
        next = request.POST.get("next", "/")
        booking = get_object_or_404(Booking, id=booking_id)
        data = Booking.objects.filter(id=booking_id)
        check_payment = 0
        try:
            check_payment = Payment.objects.get(booking_id=booking_id)
        except Payment.DoesNotExist:
            check_payment = None
        payment = check_payment
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
        pending_payment_count = Booking.objects.filter(
            guest_attended=True, bill_settled=False
        ).count()
        context = {
            "booking": booking,
            "form": form,
            "payment": payment,
            "pending_bookings": pending_bookings,
            "pending_bookings_count": pending_bookings_count,
            "pending_reviews": pending_reviews,
            "pending_reviews_count": pending_reviews_count,
            "pending_check_in_count": pending_check_in_count,
            "pending_payment_count": pending_payment_count,
        }
    else:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.booking_id = booking_id
            form.amount_tipped = float(form.amount_paid) - float(form.amount_owed)
            form.total_income = float(form.amount_paid)
            if float(form.amount_paid) < float(form.amount_owed):
                form.amount_tipped = 0
            for x in data:
                if float(form.amount_owed) <= float(form.total_income):
                    x.bill_settled = True
                    x.bill_submitted = True
                    x.save()
                elif float(form.amount_owed) > float(form.total_income):
                    x.bill_settled = False
                    x.bill_submitted = True
                    x.save()
            form.save()
            return HttpResponseRedirect(next)

    return render(request, "staff_submit_payment.html", context)
