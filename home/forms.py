from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import WeddingProfileInfo

class DateInput(forms.DateInput):
	input_type = 'date'

class SignUpForm(UserCreationForm):
	email = forms.EmailField(
		max_length=100,
		required = True,
		help_text='Enter Email Address',
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
		)
	username = forms.CharField(
		max_length=200,
		required = True,
		help_text='Enter Username',
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
		)
	password1 = forms.CharField(
		help_text='Enter Password',
		required = True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
		)
	password2 = forms.CharField(
		required = True,
		help_text='Enter Password Again',
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
		)

	class Meta:
		model = User
		fields = [
		'username', 'email', 'password1', 'password2',
		]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']




# class WeddingProfileInfoForm(forms.ModelForm):

# 	user_first_name = forms.CharField(
# 		max_length=200,
# 		required = True,
# 		help_text='Enter Username',
# 		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your First name'}),
# 		)
# 	user_partner_first_name = forms.CharField(
# 		max_length=200,
# 		required = True,
# 		help_text='Enter Username',
# 		widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Your Partner's First name"}),
# 		)
# 	# wedding_date = forms.DateTimeField(
# 	# 	help_text='Enter Password',
# 	# 	required = True,
# 	# 	widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Your Wedding Date'}),
# 	# 	)
# 	location = forms.CharField(
# 		max_length=200,
# 		required = True,
# 		help_text='Enter Username',
# 		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location... E.g Lagos Nigeria'}),
# 		)

# 	class Meta:
# 		model = WeddingProfileInfo
# 		fields = ['user_first_name', 'user_partner_first_name', 'wedding_date', 'location']
# 		widgets = {
# 		'wedding_date': DateInput(attrs={'class': 'form-control', 'placeholder': 'Your Wedding Date'}),
# 	}