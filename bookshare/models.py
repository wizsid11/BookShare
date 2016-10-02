from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Users(models.Model):
	name=models.CharField(max_length=300)
	uid=models.CharField(max_length=254)
	phone_number=models.IntegerField()
	description=models.CharField(max_length=140)
class Books(models.Model):
	name=models.CharField(max_length=300)
	author=models.CharField(max_length=300)
	uid=models.CharField(max_length=300)
	rid=models.CharField(max_length=300)
	available=models.CharField(max_length=300)
# class Available_Books(models.Model):
	# bookid=models.IntegerField()
	# uid=models.CharField(max_length=254)
# class Lease_Books(models.Model):
	# bookid=models.IntegerField()
	# uid=models.CharField(max_length=254)
