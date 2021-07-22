from django.shortcuts import render, redirect
# from .forms import SignUpForm, WeddingProfileInfoForm
# from django.contrib.auth import login as django_login, authenticate, logout
from home.models import WeddingProfileInfo
from django.contrib.auth.decorators import login_required
# from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse



@login_required(login_url='LoginPage')
def dashboard(request):

	if request.method == 'POST':

		user_first_name = request.POST.get('user_first_name')

		user_partner_first_name = request.POST.get('user_partner_first_name')
		location = request.POST.get('location')
		wedding_date = request.POST.get('wedding_date')


		WeddingProfile  = WeddingProfileInfo.objects.create(user=request.user, user_first_name=user_first_name, user_partner_first_name=user_partner_first_name, wedding_date=wedding_date, location=location)

	profile = WeddingProfileInfo.objects.get(user=request.user)

	context = {'profile': profile}

	return render(request, 'users/dashboard.html', context)


def toggle(request):
    w = WeddingProfileInfo.objects.get(id=request.POST['id'])
    w.registry = request.POST['yes'] == 'true'
    w.save()
    return HttpResponse('success')

def edit_design(request):
	return render(request, 'users/edit_design.html')

def guest_list(request):
	return render(request, 'users/guest_list.html')

def my_planner(request):

	url = 'www.google.com'

	name = 'designs/design_1.html'


	return render(request, name, url)

	

def my_preview(request):

	name = 'designs/design_1.html'

	profile = WeddingProfileInfo.objects.get(user=request.user)
	print(profile.registry)

	context = {'profile': profile}


	return render(request, name, context)

def my_registry(request):
	return render(request, 'users/my_registry.html')

def wedding_details(request):
	return render(request, 'users/wedding_details.html')



























