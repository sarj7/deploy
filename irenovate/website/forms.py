from django import forms

from .models import Contact
# , SignUp

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		widgets = {
          'details': forms.Textarea(attrs={'rows':5})
        }
		fields = ['full_name', 'email', 'phone_no', 'details']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		#email_base, provider = email.split("@")
		#domail, extension = provider.split(".")
		#if not extension == "com":
		#	raise forms.ValidationError("Please use a valid .com email address")
		# if '@' not in email:
		# 	raise forms.ValidationError("Please add @ in your email")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

	def clean_phone_no(self):
		phone_no = self.cleaned_data.get('phone_no') 
		
		if (len(phone_no) < 10 and not phone_no.isdigit()):
			raise forms.ValidationError("Please enter a valid phone number")
		
		if (len(phone_no) < 10):
			raise forms.ValidationError("Please enter a 10 digits number")	  
		
		if not phone_no.isdigit(): 
			raise forms.ValidationError("Please enter a valid phone number")
		
		return phone_no