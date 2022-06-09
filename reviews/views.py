from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect


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
            double_context = {"review": instance}
            return render(request, "review_submitted.html", double_context)
    return render(request, "create_review.html", context)
