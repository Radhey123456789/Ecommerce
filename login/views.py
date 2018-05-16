from django.shortcuts import render
from django.http import *
from django.contrib import auth
from .forms import *
from .models import *


# Create your views here.
#def index(request):
#	info=UserRegister.objects.all()
#	return render(request,'home.html',{'info':info})

def user_register(request):
	if request.method=='POST':
		form=MyForm(request.POST,request.FILES)
		if form.is_valid():
			cd=form.cleaned_data
			obj=User(username=cd['username'],email=cd['email'])
			
			obj.save()
			UserRegister.objects.create(user=obj, address=cd['address'],city=cd['city'], image=cd['image'])
			
			return HttpResponseRedirect('/')
			
	else:
		form = MyForm()
	
	
	return render(request,'login/payment.html',{'form':form})

def user_login(request):
		
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username, password=password)
		
		if user is not None:
			auth.login(request,user)
			return HttpResponseRedirect('/login/')
		else:
			return HttpResponseRedirect('/login/')
	
	return render(request, 'login/login.html')
			# Create your views here.
