from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
	email  = models.EmailField(blank=True, null=True) 
	full_name = models.CharField(max_length=120, blank=False, null=True)
	phone_no = models.CharField(max_length=13, blank=False, null=True)
	details = models.TextField( max_length=300, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)


	def __str__(self):
		return self.full_name