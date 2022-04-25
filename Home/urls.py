from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("staff/dashboard", views.staff_dashboard, name="staff-dashboard")
]