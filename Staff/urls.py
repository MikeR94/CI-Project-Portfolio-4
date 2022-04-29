
from django.urls import path
from . import views

urlpatterns = [
    path("staff/dashboard", views.staff_dashboard, name="staff_dashboard"),
    path("staff/pending-bookings", views.staff_pending_bookings, name="staff_pending_bookings"),
    path("staff/approve-booking/<booking_id>", views.staff_approve_booking, name="staff_approve_booking"),
    path("staff/deny-booking/<booking_id>", views.staff_deny_booking, name="staff_deny_booking"),
    path("staff/pending-reviews", views.staff_pending_reviews, name="staff_pending_reviews"),
    path("staff/approve-review/<review_id>", views.staff_approve_review, name="staff_approve_review"),
    path("staff/deny-review/<review_id>", views.staff_deny_review, name="staff_deny_review"),
    path("staff/details-booking/<booking_id>", views.staff_details_booking, name="staff_details_booking"),
    path("staff/all-bookings", views.staff_all_bookings, name="staff_all_bookings"),
    path("staff/all-reviews", views.staff_all_reviews, name="staff_all_reviews"),
    path("staff/check-in-page", views.staff_check_in_page, name="staff_check_in_page"),
    path("staff/check-in/<booking_id>", views.staff_check_in, name="staff_check_in"),
    path("staff/no-show/<booking_id>", views.staff_no_show, name="staff_no-show"),
    path("staff/payment-page", views.staff_payment_page, name="staff_payment_page"),
    path("staff/create-payment/<booking_id>", views.staff_create_payment, name="staff_create_payment"),
]