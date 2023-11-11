from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,"home.html")

def services(request):
    return HttpResponse('Services Page')

def products(request):
    return HttpResponse('Products Page')

def about_us(request):
    return HttpResponse('about_us Page')

def appointments(request):
    return render(request,'appointments.html')     

def contact_us(request):
    return render(request,'contact.html')          