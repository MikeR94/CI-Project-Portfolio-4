from django.shortcuts import render, get_object_or_404
from . import forms
from django.http import HttpResponseRedirect
from Reviews.models import Review


def create_review(request):
    if request.user.is_authenticated:
        form = forms.ReviewForm(request.POST or None)
        context = {
            "form": form,
            }
    else:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return render(request, "review_submitted.html")
    return render(request, "create_review.html", context)


def show_single_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    context = {
        "review": review
    }
    return render(request, "single_review.html", context)
