from django import forms

from .models import Contact
# , SignUp

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		widgets = {
          'Your_Renovation_Plan': forms.Textarea(attrs={'rows':2})
        }
		fields = ['Full_Name', 'email', 'Phone_No', 'City', 'Your_Renovation_Plan']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		#email_base, provider = email.split("@")
		#domail, extension = provider.split(".")
		#if not extension == "com":
		#	raise forms.ValidationError("Please use a valid .com email address")
		# if '@' not in email:
		# 	raise forms.ValidationError("Please add @ in your email")
		return email

	def clean_Full_Name(self):
		Full_Name = self.cleaned_data.get('Full_Name')
		return Full_Name

	def clean_Phone_No(self):
		Phone_No = self.cleaned_data.get('Phone_No') 
		
		if (len(Phone_No) < 10 and not Phone_No.isdigit()):
			raise forms.ValidationError("Please enter a valid phone number")
		
		if (len(Phone_No) < 10):
			raise forms.ValidationError("Please enter a 10 digits number")	  
		
		if not Phone_No.isdigit(): 
			raise forms.ValidationError("Please enter a valid phone number")
		
		return Phone_No