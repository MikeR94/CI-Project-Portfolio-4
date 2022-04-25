from django.shortcuts import render
from Booking.models import Booking

# Create your views here.

def index(request):
    return render(request, "index.html")

def staff_dashboard(request):
    if request.user.is_staff:
        return render(request, "staff/staff-dashboard.html")
    return render(request, "index.html")

def staff_pending_bookings(request):
    if request.user.is_staff:
        pending_bookings = Booking.objects.filter(guest_attended=False)
        context = {
            "pending_bookings": pending_bookings,
        }
        return render(request, "staff/staff-pending-bookings.html", context)