from django.contrib import admin

from .forms import ContactForm

from .models import  Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "timestamp", "updated"]
	list_display_links = ["__str__"]
	#list_editable = ["full_name"]
	#list_filter = ["updated", "timestamp"]
	search_fields = ["full_name", "phone_no"]
	
	form = ContactForm

admin.site.register(Contact, ContactAdmin)