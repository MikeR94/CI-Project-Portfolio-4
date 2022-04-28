
from django.urls import path
from . import views

urlpatterns = [
    path("staff/dashboard", views.staff_dashboard, name="staff_dashboard"),
    path("staff/pending-bookings", views.staff_pending_bookings, name="staff_pending_bookings"),
    path("staff/approve-booking/<booking_id>", views.staff_approve_booking, name="approve_booking"),
    path("staff/deny-booking/<booking_id>", views.staff_deny_booking, name="deny_booking"),
    path("staff/pending-reviews", views.staff_pending_reviews, name="staff_pending_reviews"),
    path("staff/approve/<review_id>", views.approve_review, name="staff_approve_review"),
]