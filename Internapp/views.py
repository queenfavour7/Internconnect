from django.shortcuts import render
from django.http.response import HttpResponse
from .models import department,Intern
# Create your views here.

def home(request):
    return render(request, 'index.html')

def db_view(request):  
    return render(request, 'db.html')

def navbar_component(request):
    return render(request, 'navbar.html')

def footer_component(request):
    return render(request, 'footer.html')
