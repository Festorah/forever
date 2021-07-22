from django.shortcuts import render, redirect
from .forms import SignUpForm, WeddingProfileInfoForm
from django.contrib.auth import login as django_login, authenticate, logout
from .models import WeddingProfileInfo
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse


def home(request):

	if request.method == 'POST':

		user_first_name = request.POST.get('user_first_name')
		user_partner_first_name = request.POST.get('user_partner_first_name')
		location = request.POST.get('location')
		wedding_date = request.POST.get('wedding_date')
		print(user_first_name)
		print(user_partner_first_name)
		print(location)
		print(wedding_date)



		WeddingProfile  = WeddingProfileInfo.objects.create(user=request.user, user_first_name=user_first_name, user_partner_first_name=user_partner_first_name, wedding_date=wedding_date, location=location)
		print(WeddingProfile)

	return render(request, 'home/index.html')




def signup(request):
	form  = SignUpForm()
	context = {'form': form}
	return render(request, 'home/signup.html', context)





def wedding_profile_info(request):

	if request.method == 'POST':
		sign_up_form  = SignUpForm(request.POST)

		if sign_up_form.is_valid():
			sign_up_form.save()
			username = sign_up_form.cleaned_data.get('username')
			password = sign_up_form.cleaned_data.get('password2')
			print(username)
			print(password)
			user = authenticate(request, username=username, password=password)
			if user is not None:
				django_login(request, user)
				form  = WeddingProfileInfoForm()
				context = {'form': form}
				return render(request, 'home/wedding_profile_info.html', context)
		else:
			return render(request, 'home/signup.html')


# @login_required(login_url='LoginPage')
# def dashboard(request):

# 	if request.method == 'POST':

# 		user_first_name = request.POST.get('user_first_name')

# 		user_partner_first_name = request.POST.get('user_partner_first_name')
# 		location = request.POST.get('location')
# 		wedding_date = request.POST.get('wedding_date')


# 		WeddingProfile  = WeddingProfileInfo.objects.create(user=request.user, user_first_name=user_first_name, user_partner_first_name=user_partner_first_name, wedding_date=wedding_date, location=location)

# 	profile = WeddingProfileInfo.objects.get(user=request.user)

# 	context = {'profile': profile}

# 	return render(request, 'home/dashboard.html', context)



def LoginPage(request):

	return render(request, 'home/login.html')

def Page(request):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			django_login(request, user)
			return redirect('dashboard')
	# context = {}
	return render(request, 'home/login.html')


def LogoutPage(request):

	logout(request)
	return redirect('LoginPage')


# def toggle(request):
#     w = WeddingProfileInfo.objects.get(id=request.POST['id'])
#     w.registry = request.POST['yes'] == 'true'
#     w.save()
#     return HttpResponse('success')

