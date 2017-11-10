from django.conf import settings

from django.shortcuts import render, redirect

from .models import Contact, Refer, Kitchen

from .forms import ContactForm, ReferForm, KitchenForm  

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
	 	return redirect("/acknowledgement")
	return render (request, "renovation-consultation/renovation-consultation.html", context)

def renovation(request):
	form = ContactForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	 	return redirect("/acknowledgement")
	return render (request, "renovation-consultation/renovation.html", context)

def seo_wardrobe(request):
	return render(request, "SEO/seo_wardrobe.html", {})

def seo_mumbai(request):
	return render(request, "SEO/seo_mumbai.html", {})

def renovation_ideas(request):
	return render(request, "SEO/renovation_ideas.html", {})

def kitchen_accessories(request):
	return render(request, "SEO/kitchen_accessories.html", {})

def suri_home(request):
	return render(request, "SEO/suri_home.html", {})

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
	return render(request, "Themes/Themes.html", {})

def wardrobe(request):
	form = KitchenForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	 	return redirect("/acknowledgement")
	return render(request, "Themes/Wardrobe.html", context)

def modular_kitchen(request):
	form = KitchenForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	 	return redirect("/acknowledgement")
	return render(request, "Themes/modular-kitchen.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	objects = Contact.objects.all()
	
	context = {
		"form": form,
		"objects": objects,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/acknowledgement")

	if request.user.is_staff:
		return render(request, "Contact/admin.html", context)
	else :		
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

def service(request):
	return render(request, "Footer/our-services.html", {})

def refer(request):
	form = ReferForm(request.POST or None)
	context = {
		"form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/acknowledgement")
	return render(request, "Footer/refer.html", context)

def robots(request):
	return render(request, "robots.html", {})

def sitemap(request):
	return render(request, "sitemap.html", {})