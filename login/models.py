from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserRegister(models.Model):
	user=models.OneToOneField(User)
	address=models.CharField(max_length=50)	
	city=models.CharField(max_length=50)
	image=models.FileField(upload_to='pic')
	
	def __unicode__(self):
		return self.user.username