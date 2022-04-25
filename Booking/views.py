from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect

# Create your views here.

def book_now(request):
    if request.method == "POST":
        form = forms.BookingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
            instance.save()
        return HttpResponseRedirect("/")
    form = forms.BookingForm()
    context = {
        "form": form,
        }
    return render(request, "book-now.html", context)
