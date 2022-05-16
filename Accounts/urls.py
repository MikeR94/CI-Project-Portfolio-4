from django.urls import path
from . import views


urlpatterns = [
    path("user-reservations", views.show_user_reservations, name="user_reservations"),
    path("user-details-booking/<booking_id>", views.user_details_booking, name="user_details_booking"),
    path("user-details-booking/edit/<booking_id>", views.user_edit_booking, name="edit"),
    path("user-details-booking/cancel/<booking_id>", views.user_cancel_booking, name="cancel"),
]