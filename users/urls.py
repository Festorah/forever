from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
    path('toggle/', views.toggle, name='toggle'),
    path('edit_design/', views.edit_design, name='edit-design'),
    path('my_guest_list/', views.guest_list, name='guest-list'),
    path('my_planner/', views.my_planner, name='my-planner'),
    path('my_preview/', views.my_preview, name='my-preview'),
    path('my_registry/', views.my_registry, name='my-registry'),
    path('wedding_details/', views.wedding_details, name='wedding-details'),
    ]