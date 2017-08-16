"""irenovate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import  static
from django.contrib import admin

from accounts.views import (login_view, register_view, logout_view)

from website.views import (
        home, 
        renovation_consultation,
        seo_interior,
        seo_wardrobe,
        seo_kitchen,
        renovation_ideas,
        kitchen_accessories,
        suri_home,
		ourwork,
        david,
        malibu,
        suris,
        yadav,
        retail,
        supaflex,
        themes,
        wardrobe,
        modular_kitchen,
        contact,
        privacy,
        terms,
        faq,
        career,
        disclaimer,
        acknowledge,
        service,
        refer,
    )

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^renovation-consultation$', renovation_consultation, name='renovation_consultation'),
    url(r'^renovation-consultation/interior-designers$', seo_interior, name='seo_interior'),
    url(r'^renovation-consultation/interior-wardrobes$', seo_wardrobe, name='seo_wardrobe'),
    url(r'^renovation-consultation/renovation-ideas$', renovation_ideas, name='renovation_ideas'),

    url(r'^our-work$', ourwork, name='ourwork'),
    url(r'^our-work/david$', david, name='david'),
    url(r'^our-work/malibu$', malibu, name='malibu'),
    url(r'^our-work/suris$', suris, name='suris'),
    url(r'^our-work/yadav$', yadav, name='yadav'),
    url(r'^our-work/retail$', retail, name='retail'),
    url(r'^our-work/supaflex$', supaflex, name='supaflex'),
    url(r'^our-work/suri-home$', suri_home, name='suri_home'),

    url(r'^themes$', themes, name='themes'),

    url(r'^wardrobes$', wardrobe, name='wardrobe'),

    url(r'^modular-kitchen$', modular_kitchen, name='modular_kitchen'),
    url(r'^modular-kitchen/interior-kitchen$', seo_kitchen, name='seo_kitchen'),
    url(r'^modular-kitchen/kitchen-accessories$', kitchen_accessories, name='kitchen_accessories'),
    
    url(r'^contact-us$', contact, name='contact'),

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^privacy-policy$', privacy, name='privacy'),
    url(r'^terms-and-conditions$', terms, name='terms'),
    url(r'^faqs$', faq, name='faq'),
    url(r'^career$', career, name='career'),
    url(r'^disclaimer$', disclaimer, name='disclaimer'),
    url(r'^acknowledgement$', acknowledge, name='acknowledge'),
    url(r'^our-service$', service, name='service'),
    url(r'^refer-a-friend$', refer, name='refer'),

    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)