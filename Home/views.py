from django.shortcuts import render
from Reviews.models import Review

# Create your views here.


def index(request):
    reviews = Review.objects.filter(approved=True).order_by("?")[:4]
    stars = 3
    context = {
        "reviews": reviews,
        "stars": stars
        }

    return render(request, "index.html", context)


def gallery(request):
    return render(request, "gallery.html")
