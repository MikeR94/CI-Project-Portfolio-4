from django.urls import path
from . import views


urlpatterns = [
    path("create/review", views.create_review, name="create_review"),
    path("review/<review_id>", views.show_single_review, name="single_review"),
]
