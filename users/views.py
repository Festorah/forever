from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate, logout
# from .forms import SignUpForm, WeddingProfileInfoForm
# from django.contrib.auth import login as django_login, authenticate, logout
from .models import MyWebsite
from django.contrib.auth.decorators import login_required
# from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
from home.forms import SignUpForm



@login_required(login_url='LoginPage')
def dashboard(request):

	mywebsite, created = MyWebsite.objects.get_or_create(user=request.user)


	if request.method == 'POST':

		sign_up_form  = SignUpForm(request.POST)

		#Introduction
		bride_name = request.POST.get('bride_name')
		groom_name = request.POST.get('groom_name')
		about_bride = request.POST.get('about_bride')
		about_groom = request.POST.get('about_groom')
		wedding_date = request.POST.get('wedding_date')
		location = request.POST.get('location')
		bride_image = request.FILES.get('bride_image')
		groom_image = request.FILES.get('groom_image')

		#Hero images
		hero_images = request.FILES.getlist('hero_images')

		#Our story
		how_we_met = request.POST.get('how_we_met')
		first_outing = request.POST.get('first_outing')
		proposal = request.POST.get('proposal')
		courtship = request.POST.get('courtship')
		together_forever = request.POST.get('together_forever')

		#Gallery
		gallery = request.FILES.getlist('gallery')

		#Wedding Events
		wedding_engagement_date = request.POST.get('wedding_engagement_date')
		wedding_engagement_time = request.POST.get('wedding_engagement_time')
		wedding_engagement_venue = request.POST.get('wedding_engagement_venue')
		wedding_engagement_description = request.POST.get('wedding_engagement_description')

		wedding_reception_time = request.POST.get('wedding_reception_time')
		wedding_reception_venue = request.POST.get('wedding_reception_venue')
		wedding_reception_description = request.POST.get('wedding_reception_description')

		wedding_ceremony_time = request.POST.get('wedding_ceremony_time')
		wedding_ceremony_venue = request.POST.get('wedding_ceremony_venue')
		wedding_ceremony_description = request.POST.get('wedding_ceremony_description')

		if sign_up_form != None:
			if sign_up_form.is_valid():
				sign_up_form.save()
				username = sign_up_form.cleaned_data.get('username')
				password = sign_up_form.cleaned_data.get('password2')
				print(username)
				print(password)
				user = authenticate(request, username=username, password=password)
				if user is not None:
					django_login(request, user)
					# form  = WeddingProfileInfoForm()
					# context = {'form': form}
					return render(request, 'users/dashboard.html')

		if hero_images != list() or wedding_date != None:
			print(wedding_date)
			print(hero_images)
			mywebsite.wedding_date = wedding_date
			n = len(hero_images)
			for image in hero_images:
				if n ==3:
					mywebsite.hero_image_1 = image
				elif n==2:
					mywebsite.hero_image_2 = image
				else:
					mywebsite.hero_image_3 = image
				n -= 1

		if bride_name != None:
			mywebsite.bride_name = bride_name
			print(bride_name)
			mywebsite.bride_image = bride_image
			mywebsite.about_groom = about_groom
			print(about_groom)

		elif groom_name != None:
			print(groom_name)
			mywebsite.groom_name = groom_name
			mywebsite.groom_image = groom_image
			mywebsite.about_bride = about_bride

		if how_we_met != None or first_outing != None:
			# if how_we_met != '':
			print(how_we_met)
			print(first_outing)
			print('good groom')
			mywebsite.how_we_met = how_we_met
			mywebsite.first_outing = first_outing
			mywebsite.proposal = proposal
			mywebsite.courtship = courtship
			mywebsite.together_forever = together_forever

		if gallery != None:
			n = len(gallery)
			for image in gallery:
				if n ==6:
					mywebsite.gallery_1 = image
				elif n==5:
					mywebsite.gallery_2 = image
				if n ==4:
					mywebsite.gallery_3 = image
				elif n==3:
					mywebsite.gallery_4 = image
				elif n==2:
					mywebsite.gallery_5 = image
				else:
					mywebsite.gallery_6 = image
				n -= 1

		# if gallery != None:
		# 	mywebsite.gallery_1 = gallery[0]
		# 	mywebsite.gallery_2 = gallery[1]
		# 	mywebsite.gallery_3 = gallery[2]
		# 	mywebsite.gallery_4 = gallery[3]
		# 	mywebsite.gallery_5 = gallery[4]
		# 	mywebsite.gallery_6 = gallery[5]

		if wedding_engagement_date != '':
			mywebsite.wedding_engagement_date = wedding_engagement_date
			mywebsite.wedding_engagement_time = wedding_engagement_time
			mywebsite.wedding_engagement_venue = wedding_engagement_venue
			mywebsite.wedding_engagement_description = wedding_engagement_description

		if wedding_ceremony_time != '':
			mywebsite.wedding_ceremony_time = wedding_ceremony_time
			mywebsite.wedding_ceremony_venue = wedding_ceremony_venue
			mywebsite.wedding_ceremony_description = wedding_ceremony_description

		if wedding_reception_time != '':
			mywebsite.wedding_reception_time = wedding_reception_time
			mywebsite.wedding_reception_venue = wedding_reception_venue
			mywebsite.wedding_reception_description = wedding_reception_description

	mywebsite.save()

	context = {'mywebsite': mywebsite}

	return render(request, 'users/dashboard.html', context)


def toggle(request):
    # w = WeddingProfileInfo.objects.get(id=request.POST['id'])
    # w.registry = request.POST['yes'] == 'true'
    # w.save()
    return HttpResponse('success')

def edit_design(request):
	return render(request, 'users/edit_design.html')

def guest_list(request):
	return render(request, 'users/guest_list.html')

def my_planner(request):

	url = 'www.google.com'

	name = 'designs/design_1.html'


	return render(request, name)

	

def my_preview(request):

	mywebsite = MyWebsite.objects.get(user=request.user)

	name = mywebsite.web_design_template

	temp_name = 'designs/' + str(name) + '.html'

	

	context = {'mywebsite': mywebsite}


	return render(request, temp_name, context)

def my_registry(request):
	return render(request, 'users/my_registry.html')

def wedding_details(request):
	return render(request, 'users/wedding_details.html')


def my_wedding_website(request, slug):
	print(slug)

	mywebsite = MyWebsite.objects.get(slug=slug)

	name = mywebsite.web_design_template

	mywebsite.slug = str(mywebsite.slug)

	temp_name = 'designs/' + str(name) + '.html'



	if request.method == 'POST':
		
		comment_name = request.POST.get('comment_name')
		comment_message = request.POST.get('comment_message')

		if name != '':
		
			name = request.POST.get('name')
			email = request.POST.get('email')
			number_of_guest = request.POST.get('number_of_guest')
			attending = request.POST.get('attending')
			message = request.POST.get('message')

		# if comment_name != '':
		
		# 	comment_name = request.POST.get('comment_name')
		# 	comment_message = request.POST.get('comment_message')

			print(name)
			print(email)
			print(number_of_guest)
			print(attending)
			print(message)
			print(comment_name)
			print(comment_message)
		



	context = {
		'mywebsite': mywebsite,
		'mywebsite.slug': mywebsite.slug,
		}

	return render(request, temp_name, context)









	# return render(request, 'users/dashboard.html', context)
























