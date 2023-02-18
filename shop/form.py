from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'Enter Your Name'}))
	email=forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'Enter email address'}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control','placeholder':'Enter Your password'}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'from-control','placeholder':'Confirm Your password'}))
	class Meta:
		model=User
		fields=['username','email','password1','password2']