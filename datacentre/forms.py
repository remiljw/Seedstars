from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
#importing our ModelForms from django
from .models import *
#importing your models from models.py
class SignupForm(ModelForm):
	class Meta:
    #to specify the model and field that is being imported into the class SignupForm 
		model = UserDetails
		fields = ['first_name','last_name','email','gender']

		# this function will be used for the validation 

