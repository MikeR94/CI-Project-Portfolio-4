from django.urls import path
from . import views


urlpatterns = [
    path("book-now", views.book_now, name="book-now"),
]