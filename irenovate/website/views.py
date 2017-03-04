from django.conf import settings

from django.shortcuts import render, redirect

from .forms import ContactForm   

def home(request):
	return render(request, "home.html", {})

def renovation_consultation(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)

		instance.save()
	 	
		return redirect("/acknowledge")
	return render (request, "renovation-consultation.html", context)

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

def supaflex(request):
	return render(request, "supaflex.html", {})

def themes(request):
	return render(request, "themes.html", {})

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}

	if form.is_valid():
	 	instance = form.save(commit=False)

	 	instance.save()

	 	return redirect("/acknowledge")

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

def acknowledge(request):
	return render(request, "acknowledge.html", {})