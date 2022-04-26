from django.urls import path
from . import views


urlpatterns = [
    path("user-reservations", views.show_user_reservations, name="user_reservations"),
]