from django import forms
from django.contrib.auth.models import User
from .models import *

class MyForm(forms.ModelForm):
	
	address= forms.CharField(max_length=50, required=False)
	city= forms.CharField(max_length=50)
	image=forms.FileField()
	
	class Meta:
		model=User
		fields=['username','email','password','address','city','image']
		