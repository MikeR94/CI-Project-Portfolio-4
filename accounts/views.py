from django.shortcuts import render, get_object_or_404, redirect
from booking.forms import BookingForm
from booking.models import Booking
from django.http import HttpResponseRedirect
from staff.models import Payment
from django.contrib import messages


def show_user_reservations(request):
    """
    Render the user reservations page
    """
    if request.user.is_authenticated:
        booking = Booking.objects.filter(
            user=request.user, guest_attended=False, guest_no_show=False
        )
        completed_booking = Booking.objects.filter(
            user=request.user,
            guest_attended=True,
            guest_no_show=False,
        )
        no_show_booking = Booking.objects.filter(
            user=request.user, guest_no_show=True, guest_attended=False
        )
        no_show_booking_count = Booking.objects.filter(
            user=request.user, guest_no_show=True
        ).count()
        completed_booking_count = Booking.objects.filter(
            user=request.user, guest_attended=True
        ).count()
        total_completed_booking_count = int(no_show_booking_count) + int(
            completed_booking_count
        )
        context = {
            "booking": booking,
            "no_show_booking": no_show_booking,
            "completed_booking": completed_booking,
            "completed_booking_count": total_completed_booking_count,
        }
        return render(request, "user_reservations.html", context)
    return HttpResponseRedirect("accounts/login")


def user_details_booking(request, booking_id):
    """
    Render the user details booking page
    which shows additional information
    about a users booking
    """
    if request.user.is_authenticated:
        next = request.POST.get("next", "/")
        booking = Booking.objects.filter(id=booking_id)
        booking_data = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST or None, instance=booking_data)
        check_payment = 0
        try:
            check_payment = Payment.objects.get(booking_id=booking_id)
        except Payment.DoesNotExist:
            check_payment = None
        payment = check_payment
        context = {
            "booking": booking_data,
            "form": form,
            "payment": payment,
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
                number_of_guests=instance.number_of_guests,
                email=instance.email,
                contact_number=instance.contact_number,
                additional_info=instance.additional_info,
                disabled_access=instance.disabled_access,
            ).exists():
                messages.add_message(
                    request,
                    messages.ERROR,
                    f"Duplicate Booking - Booking already in the calendar.",
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
                f"Your booking has been updated successfully!.",
            )

            return HttpResponseRedirect(next)
        messages.add_message(
            request,
            messages.ERROR,
            f"Error updating the booking, please try again.",
        )
    return render(request, "user_details_booking.html", context)


def user_cancel_booking(request, booking_id):
    """
    Function to cancel a booking and
    remove it from the database
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        booking.delete()
        return redirect("user_reservations")
    else:
        return HttpResponseRedirect("/")
