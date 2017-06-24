from django.contrib import admin

from .forms import ContactForm, ReferForm, KitchenForm

from .models import  Contact, Refer, Kitchen

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email", "timestamp", "updated"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name", "Phone_No"]
	
	form = ContactForm

class KitchenAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name"]
	
	form = KitchenForm

class ReferAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email"]
	list_display_links = ["__str__"]
	search_fields = ["Full_Name"]
	
	form = ReferForm

admin.site.register(Contact, ContactAdmin)
admin.site.register(Kitchen, KitchenAdmin)
admin.site.register(Refer, ReferAdmin)