from django.conf import settings

from django.shortcuts import render, redirect

from .forms import ContactForm   

def home(request):
	return render(request, "Home/home.html", {})

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

def ourwork(request):
	return render(request, "OurWork/ourwork.html", {})

def david(request):
	return render(request, "OurWork/david.html", {})

def malibu(request):
	return render(request, "OurWork/malibu.html", {})

def suris(request):
	return render(request, "OurWork/suris.html", {})

def yadav(request):
	return render(request, "OurWork/yadav.html", {})

def retail(request):
	return render(request, "OurWork/retail.html", {})

def supaflex(request):
	return render(request, "OurWork/supaflex.html", {})

def themes(request):
	return render(request, "Themes/themes.html", {})

def wardrobe(request):
	return render(request, "Themes/Wardrobe.html", {})

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}

	if form.is_valid():
	 	instance = form.save(commit=False)

	 	instance.save()

	 	return redirect("/acknowledge")

	return render(request, "Contact/contact-us.html", context)

def privacy(request):
	return render (request, "Footer/privacy.html", {})

def terms(request):
	return render (request, "Footer/terms.html", {})

def faq(request):
	return render (request, "Footer/faq.html", {})

def career(request):
	return render (request, "Footer/career.html", {})

def disclaimer(request):
	return render (request, "Footer/disclaimer.html", {})

def acknowledge(request):
	return render(request, "acknowledge.html", {})