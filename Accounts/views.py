from django.shortcuts import render
from Booking.models import Booking

# Create your views here.

def show_user_reservations(request):
    test = Booking.objects.filter(user=request.user)
    context = {
        "test": test
    }
    return render(request, "user_reservations.html", context)