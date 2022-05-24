from django.shortcuts import render, get_object_or_404, redirect
from Booking.forms import BookingForm
from Booking.models import Booking
from django.http import HttpResponseRedirect

# Create your views here.

def show_user_reservations(request):
    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user)
        context = {
            "booking": booking
        }
        return render(request, "user_reservations.html", context)
    return HttpResponseRedirect("/")


def user_details_booking(request, booking_id):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        context = {
            "booking": booking,
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
            for item in booking:
                item.booking_approved = False
                item.booking_acknowledged = False
                item.save()
            instance.save()
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
