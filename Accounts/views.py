from django.shortcuts import render, get_object_or_404, redirect
from Booking.models import Booking
from django.http import HttpResponseRedirect
from Staff.forms import EditBookingForm

# Create your views here.

def show_user_reservations(request):
    booking = Booking.objects.filter(user=request.user)
    context = {
        "booking": booking
    }
    return render(request, "user_reservations.html", context)


def user_details_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        "booking": booking,
    }
    return render(request, "user_details_booking.html", context)


def user_edit_booking(request, booking_id):
    booking_data = get_object_or_404(Booking, id=booking_id)
    booking = Booking.objects.filter(id=booking_id)
    next = request.POST.get("next", "/")
    if request.method == "POST":
        form = EditBookingForm(request.POST, instance=booking_data)
        if form.is_valid():
            form.save()
            for item in booking:
                item.booking_approved = False
                item.booking_acknowledged = False
                item.save()
            return HttpResponseRedirect(next)
    form = EditBookingForm(instance=booking_data)
    context = {
        "booking": booking,
        "form": form
    }
    return render(request, "user_edit_booking.html", context)


def user_cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect("user_reservations")
