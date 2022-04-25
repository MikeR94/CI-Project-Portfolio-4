from django.shortcuts import render
from Booking.models import Booking
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "index.html")


def staff_dashboard(request):
    if request.user.is_staff:
        return render(request, "staff/staff-dashboard.html")
    return render(request, "index.html")


def staff_pending_bookings(request):
    if request.user.is_staff:
        pending_bookings = Booking.objects.filter(booking_approved=False)
        context = {
            "pending_bookings": pending_bookings,
        }
        return render(request, "staff/staff-pending-bookings.html", context)


def staff_approve_booking(request, booking_id):
    next = request.POST.get("next", "/")
    booking = Booking.objects.filter(id=booking_id)
    for object in booking:
        object.booking_approved = True
        object.save()
    return HttpResponseRedirect(next)