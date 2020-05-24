from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from home.models import UserProfile
from django.forms import FileInput

class UserUpdateForm(UserChangeForm):

	class Meta:
		model=User
		fields=('username', 'email', 'first_name', 'last_name',)

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model=UserProfile
		fields=('phone', 'city', 'country', 'image',)
		
