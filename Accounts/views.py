from django.shortcuts import render, get_object_or_404, redirect
from requests import get
from Booking.forms import BookingForm
from Booking.models import Booking
from django.http import HttpResponseRedirect
from Staff.models import Payment
from django.contrib import messages

# Create your views here.


def show_user_reservations(request):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(
            user=request.user, guest_attended=False
        )
        completed_booking = Booking.objects.filter(
            user=request.user, guest_attended=True
        )
        completed_booking_count = Booking.objects.filter(
            user=request.user, guest_attended=True
        ).count()
        context = {
            "booking": booking,
            "completed_booking": completed_booking,
            "completed_booking_count": completed_booking_count,
        }
        return render(request, "user_reservations.html", context)
    return HttpResponseRedirect("/")


def user_details_booking(request, booking_id):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        booking_data = get_object_or_404(Booking, id=booking_id)
        next = request.POST.get("next", "/")
        form = BookingForm(request.POST or None, instance=booking_data)
        check_payment = 0
        try:
            check_payment = Payment.objects.get(booking_id=booking_id)
        except Payment.DoesNotExist:
            check_payment = None
        payment = check_payment
        context = {
            "booking": booking,
            "payment": payment,
            "form": form,
        }
        return render(request, "user_details_booking.html", context)

    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            double_context = {
                "data": instance,
            }
            if Booking.objects.filter(
                first_name=instance.first_name,
                last_name=instance.last_name,
                time_of_visit=instance.time_of_visit,
                date_of_visit=instance.date_of_visit,
            ).exists():
                return render(
                    request, "book_double_error.html", double_context
                )
            instance.save()
            for item in booking:
                item.booking_approved = False
                item.booking_acknowledged = False
                item.booking_denied = False
                item.save()
            return HttpResponseRedirect(next)
    return HttpResponseRedirect("accounts/login")


def user_edit_booking(request, booking_id):
    if request.user.is_authenticated:
        next = request.POST.get("next", "/")
        booking = Booking.objects.filter(id=booking_id)
        booking_data = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST or None)
        context = {
                "booking": booking_data,
                "form": form,
            }
    else:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            if Booking.objects.filter(
                first_name=instance.first_name,
                last_name=instance.last_name,
                time_of_visit=instance.time_of_visit,
                date_of_visit=instance.date_of_visit,
            ).exists():
                messages.add_message(
                    request,
                    messages.ERROR,
                    f"Jack is double booking now.",
                )
                return HttpResponseRedirect(next)
            instance.save()
            for item in booking:
                item.booking_approved = False
                item.booking_acknowledged = False
                item.booking_denied = False
                item.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Jack is the really the greatest.",
            )
            double_context = {
                "booking": instance,
                "form": form,
            }
            return render(request, "user_details_booking.html", double_context)
    messages.add_message(
        request,
        messages.ERROR,
        f"Jack is the greatest.",
    )
    return render(request, "user_details_booking.html", context)


def user_cancel_booking(request, booking_id):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect("user_reservations")
    else:
        return HttpResponseRedirect("/")
