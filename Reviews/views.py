from django.shortcuts import render, get_object_or_404
from . import forms
from django.http import HttpResponseRedirect
from Reviews.models import Review

# Create your views here.


def create_review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.ReviewForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            return HttpResponseRedirect("/")
        form = forms.ReviewForm()
        context = {
            "form": form,
            }
        return render(request, "create_review.html", context)
    else:
        return HttpResponseRedirect("/")


def show_single_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    context = {
        "review": review
    }
    return render(request, "single_review.html", context)
