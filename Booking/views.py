from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms

# Create your views here.

def book_now(request):
    form = forms.BookingForm(request.POST or None)
    context = {
        "form": form,
        }
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            instance.save()
            success_context = {
                "data": instance,
            }
            return render(request, "book_success.html", success_context)
    return render(request, "book_now.html", context)

