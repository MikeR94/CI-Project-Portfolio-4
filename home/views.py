from django.shortcuts import render
from reviews.models import Review


def index(request):
    """
    Renders the home page and passes
    in the data to render 4 approved
    review cards randomly
    """
    reviews = Review.objects.filter(approved=True).order_by("?")[:4]
    context = {
        "reviews": reviews,
    }

    return render(request, "index.html", context)


def gallery(request):
    """
    Renders the gallery page
    """
    return render(request, "gallery.html")
