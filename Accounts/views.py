from django.shortcuts import render, get_object_or_404, redirect
from Booking.models import Booking
from django.http import HttpResponseRedirect
from Staff.forms import EditBookingForm

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
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        "booking": booking,
    }
    return render(request, "user_details_booking.html", context)


def user_edit_booking(request, booking_id):
    if request.user.is_authenticated:
        booking_data = get_object_or_404(Booking, id=booking_id)
        booking = Booking.objects.filter(id=booking_id)
        if request.method == "POST":
            form = EditBookingForm(request.POST, instance=booking_data)
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
        form = EditBookingForm(instance=booking_data)
        context = {
            "booking": booking,
            "form": form
        }
        return render(request, "user_edit_booking.html", context)
    else:
        return HttpResponseRedirect("/")


def user_cancel_booking(request, booking_id):
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect("user_reservations")
    else:
        return HttpResponseRedirect("/")
