from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def home(request):
	return render(request, 'dcn/home.html')

def contact(request):
	if request.method == "POST":

		c = Contacts()
		c.name = request.POST.get('name')
		c.email = request.POST.get('email')
		c.subject = request.POST.get('subject')
		c.message = request.POST.get('message')
		c.save()
		messages.success(request, 'Thank you for Contacting Us. You will hear from us soon!')

		return render(request, 'dcn/home.html')
	else:
		return render(request, 'dcn/home.html')

