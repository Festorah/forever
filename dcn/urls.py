from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dcn-home'),
    path('contact/', views.contact, name='dcn-contact'),
]