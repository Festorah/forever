from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('create_wedding_info/', views.wedding_profile_info, name='wedding-info'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
    path('Page/', views.Page, name='Page'),
    ]