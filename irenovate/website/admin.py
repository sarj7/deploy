from django.contrib import admin

from .forms import ContactForm

from .models import  Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "timestamp", "updated"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name", "Phone_No"]

	form = ContactForm

admin.site.register(Contact, ContactAdmin)