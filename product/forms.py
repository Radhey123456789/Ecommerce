from django import forms
from django.contrib.auth.models import User
from .models import *

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class NewCart(forms.ModelForm):
	class Meta:
		model=Cart
		fields=['quantity']

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model=User
		fields=['username','email','password']
		