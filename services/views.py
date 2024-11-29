from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    
    servi = Service.objects.all()
    
    return render(request,"services/services.html", {"services": servi})