from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("staff/dashboard", views.staff_dashboard, name="staff_dashboard"),
    path("staff/pending-bookings", views.staff_pending_bookings, name="staff_pending_bookings"),
    path("staff/approve-booking/<booking_id>", views.staff_approve_booking, name="approve_booking"),
    path("staff/deny-booking/<booking_id>", views.staff_deny_booking, name="deny_booking"),
]