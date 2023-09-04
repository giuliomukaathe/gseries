from django.shortcuts import render
from .models import StaffMember

def home(request):
    return render(request, "index.html")

def staff(request):
    StaffMembers = StaffMember.objects.all()
    return render(request, 'index.html', {'StaffMembers': StaffMembers})
