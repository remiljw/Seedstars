from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Gender(models.Model):
	sex = models.CharField(max_length=50, default=None) 
	def __str__(self):
		return self.sex
	class Meta:
		verbose_name_plural = "Gender"

class UserDetails(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50) 
	email = models.EmailField(max_length=50)
	gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)


	def __str__(self):
		return self.first_name
	class Meta:
		verbose_name_plural = "User Details"
