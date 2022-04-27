from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect

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
        context = {"form": form}
        return render(request, "create_review.html", context)
    else:
        return HttpResponseRedirect("/")
