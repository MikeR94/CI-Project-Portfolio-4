from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("staff/dashboard", views.staff_dashboard, name="staff-dashboard"),
    path("staff/pending-bookings", views.staff_pending_bookings, name="staff-pending-bookings"),
]