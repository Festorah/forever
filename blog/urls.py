from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('port_folio/', views.port_folio, name='blog-portfolio'),
    path('invite/', views.invite, name='blog-portfolio'),

]