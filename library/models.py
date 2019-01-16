from django.db import models
import uuid
from django.shortcuts import reverse
# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=150, help_text='Enter the titleof your book')
	author = models.ForeignKey('Author', on_delete = models.CASCADE)
	genre = models.CharField(max_length=50, help_text='Enter the book genre')
	id = models.UUIDField(primary_key = True, default= uuid.uuid4)
	year_of_prod = models.DateField(auto_now = False)
	isbn = models.CharField(max_length=13, help_text='Enter your 13 characters ISBN')
	pics = models.ImageField(upload_to = 'C/User/Desktop', max_length=200)
	image = models.ImageField(upload_to='images/', null=True)

	def __str__(self):
		return self.title

class Author(models.Model):
	first_name = models.CharField(max_length=200, help_text='Enter your First Name')
	last_name = models.CharField(max_length=150, help_text='Enter your last Name')
	date_of_birth = models.DateField(auto_now=False)
	pic = models.ImageField(upload_to=None)
	picss = models.ImageField(upload_to='media/')
	pcs = models.ImageField(upload_to='images/', null = True)
	image = models.ImageField(upload_to='images/', null =True)
	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' : ' + str(self.pcs)

class Image(models.Model):
	image = models.ImageField(upload_to='image/', null=True)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name 