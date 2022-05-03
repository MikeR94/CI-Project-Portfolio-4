from django.urls import path
from . import views


urlpatterns = [
    path("user-reservations", views.show_user_reservations, name="user_reservations"),
    path("user-edit-booking/<booking_id>", views.user_edit_booking, name="user_edit_booking"),
]