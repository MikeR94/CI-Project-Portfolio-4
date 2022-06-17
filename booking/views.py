from django.http import HttpResponseRedirect
from django.shortcuts import render
from booking.models import Booking
from booking.forms import BookingForm


def book_now(request):
    """
    This function handles when a
    guest makes a booking on the website
    """
    if request.user.is_authenticated:
        form = BookingForm(request.POST or None)
        context = {
            "form": form,
        }
    else:
        return HttpResponseRedirect("accounts/login")
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
                    request, "book_double_error.html", double_context)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            instance.save()
            success_context = {
                "data": instance,
            }
            return render(request, "book_success.html", success_context)
    return render(request, "book_now.html", context)
