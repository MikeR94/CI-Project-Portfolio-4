from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def staff_dashboard(request):
    if request.user.is_staff:
        return render(request, "staff/staff-dashboard.html")
    return render(request, "index.html")