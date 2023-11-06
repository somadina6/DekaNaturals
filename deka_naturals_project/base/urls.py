from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('about-us/', views.about_us, name="about-us"),
    path('appointments', views.appointments, name='appointments'),

]

