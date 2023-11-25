from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.





def home(request):
    return render(request,"home.html")

def services(request):
    return HttpResponse('services page')

def products(request):
    products = models.Multivitamins.objects.values()
    context = {'products': products}
    return render(request, 'products.html', context)

def about_us(request):
    return HttpResponse('about_us Page')

def appointments(request):
    return render(request,'appointments.html')     

def contact_us(request):
    return render(request,'contact.html')          