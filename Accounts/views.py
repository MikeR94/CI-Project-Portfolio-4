from django.shortcuts import render, get_object_or_404, redirect
from Booking.forms import BookingForm
from Booking.models import Booking
from django.http import HttpResponseRedirect
from Staff.models import Payment

# Create your views here.

def show_user_reservations(request):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user, guest_attended=False)
        completed_booking = Booking.objects.filter(user=request.user, guest_attended=True)
        completed_booking_count = Booking.objects.filter(user=request.user, guest_attended=True).count()
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
        check_payment = 0
        try:
            check_payment = Payment.objects.get(booking_id=booking_id)
        except Payment.DoesNotExist:
            check_payment = None
        payment = check_payment
        context = {
            "booking": booking,
            "payment": payment,
        }
        return render(request, "user_details_booking.html", context)
    return HttpResponseRedirect("accounts/login")


def user_edit_booking(request, booking_id):
    if request.user.is_authenticated:
        booking_data = get_object_or_404(Booking, id=booking_id)
        booking = Booking.objects.filter(id=booking_id)
        form = BookingForm(request.POST or None, instance=booking_data)
        context = {
        "booking": booking,
        "form": form
        }
    else:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            double_context = {
                "data": instance,
            }
            if Booking.objects.filter(first_name=instance.first_name, last_name=instance.last_name, time_of_visit=instance.time_of_visit, date_of_visit=instance.date_of_visit).exists():
                return render(request, "book_double_error.html", double_context)
            instance.save()
            for item in booking:
                item.booking_approved = False
                item.booking_acknowledged = False
                item.booking_denied = False
                item.save()
            success_context = {
                "data": instance,
            }
            return render(request, "user_edit_booking_success.html", success_context)
    return render(request, "user_edit_booking.html", context)


def user_cancel_booking(request, booking_id):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect("user_reservations")
    else:
        return HttpResponseRedirect("/")
