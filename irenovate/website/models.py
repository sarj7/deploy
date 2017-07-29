from __future__ import unicode_literals

from django.db import models

CITY_CHOICES = (
	('BANGALORE','Bangalore'),
	('DELHI/ncr','Delhi/NCR'),
	('JAIPUR', 'Jaipur'),
	('MUMBAI','Mumbai'),
)

class Contact(models.Model):
	email = models.EmailField(blank=True, null=True) 
	Full_Name = models.CharField(max_length=120, blank=False, null=True)
	Phone_No = models.CharField(max_length=13, blank=False, null=True)
	City = models.CharField(max_length=200, choices=CITY_CHOICES, blank=False, default='DELHI/ncr')
	Your_Renovation_Plan = models.TextField( max_length=300, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.Full_Name


class Kitchen(models.Model):
	email = models.EmailField(blank=True, null=True)
	Full_Name = models.CharField(max_length=120, blank=False, null=True)
	Phone_No = models.CharField(max_length=13, blank=False, null=True)
	City = models.CharField(max_length=200, choices=CITY_CHOICES, blank=False, default='DELHI/ncr')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.Full_Name


class Refer(models.Model):
	Full_Name = models.CharField(max_length=120, blank=False)
	email = models.EmailField(blank=True, null=True) 
	Friend_Name = models.CharField(max_length=120, blank=False)
	Friend_Email = models.EmailField(blank=True, null=True)
	Phone_No = models.CharField(max_length=13, blank=False, null=True)
	City = models.CharField(max_length=200, choices=CITY_CHOICES, blank=False, default='DELHI/ncr')
	Renovation_Plan = models.TextField( max_length=300, blank=False, null=True)

	def __str__(self):
		return self.Full_Name
	