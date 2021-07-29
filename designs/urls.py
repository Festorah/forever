from django.urls import path
from . import views

urlpatterns = [
    path('', views.templates, name='templates-home'),
    path('<slug:slug>/', views.template_sample_preview, name='template-sample-preview'),
    ]

