from django.contrib import admin

from .forms import ContactForm, ReferForm

from .models import  Contact, Refer

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "timestamp", "updated"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name", "Phone_No"]
	
	form = ContactForm

class ReferAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name"]
	
	form = ReferForm

admin.site.register(Contact, ContactAdmin)
admin.site.register(Refer, ReferAdmin)