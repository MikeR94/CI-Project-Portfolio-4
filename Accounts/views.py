from django.shortcuts import render, get_object_or_404
from Booking.models import Booking

# Create your views here.

def show_user_reservations(request):
    booking = Booking.objects.filter(user=request.user)
    context = {
        "booking": booking
    }
    return render(request, "user_reservations.html", context)


def user_edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        "booking": booking,
    }
    return render(request, "user_edit_booking.html", context)
