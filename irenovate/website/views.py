from django.conf import settings

from django.shortcuts import render, redirect

from .forms import ContactForm   

def home(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)

	# 	full_name = form.cleaned_data.get("full_name")
	#	if not full_name:
	# 		full_name = "New full name"
	# 	instance.full_name = full_name
	# 	if not instance.full_name:
	# 	 	instance.full_name = "Justin"
		instance.save()
	 	
	# if request.user.is_authenticated() and request.user.is_staff:
	# 	print(SignUp.objects.all())
	# 	i = 1
	# 	for instance in SignUp.objects.all():
	# 	 	print(i)
	# 	 	print(instance.full_name)
	# 	 	i += 1

	# 	queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
	# 	print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
	# 	context = {
	# 		"queryset": queryset
	# 	}
		return redirect("/")
	return render(request, "home.html", context)

def design(request):
	return render (request, "renovation-consultation.html", {})

def gallery(request):
	return render(request, "gallery.html", {})

def david(request):
	return render(request, "david.html", {})

def malibu(request):
	return render(request, "malibu.html", {})

def suris(request):
	return render(request, "suris.html", {})

def yadav(request):
	return render(request, "yadav.html", {})

def retail(request):
	return render(request, "retail.html", {})


def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}

	if form.is_valid():
	# 	form.save()
	# 	print request.POST['email'] #not recommended
	 	instance = form.save(commit=False)

	# 	full_name = form.cleaned_data.get("full_name")
	#	if not full_name:
	# 		full_name = "New full name"
	# 	instance.full_name = full_name
	# 	if not instance.full_name:
	# 	 	instance.full_name = "Justin"
	 	instance.save()
	 	
	# if request.user.is_authenticated() and request.user.is_staff:
	# 	print(SignUp.objects.all())
	# 	i = 1
	# 	for instance in SignUp.objects.all():
	# 	 	print(i)
	# 	 	print(instance.full_name)
	# 	 	i += 1

	# 	queryset = SignUp.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
	# 	print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
	# 	context = {
	# 		"queryset": queryset
	# 	}

	return render(request, "contact-us.html", context)

def privacy(request):
	return render (request, "privacy.html", {})

def terms(request):
	return render (request, "terms.html", {})

def faq(request):
	return render (request, "faq.html", {})

def career(request):
	return render (request, "career.html", {})

def disclaimer(request):
	return render (request, "disclaimer.html", {})