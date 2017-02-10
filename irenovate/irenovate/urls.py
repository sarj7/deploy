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
        design, 
        gallery,
        david,
        malibu,
        suris,
        yadav,
        retail, 
        contact,
        privacy,
        terms,
        faq,
        career,
        disclaimer,
        acknowledge,
    )

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^renovation-consultation$', design, name='design'),
    
    url(r'^our_work$', gallery, name='gallery'),
    url(r'^our_work/david$', david, name='david'),
    url(r'^our_work/malibu$', malibu, name='malibu'),
    url(r'^our_work/suris$', suris, name='suris'),
    url(r'^our_work/yadav$', yadav, name='yadav'),
    url(r'^our_work/retail$', retail, name='retail'),
    
    url(r'^contact$', contact, name='contact'),

    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),

    url(r'^privacy$', privacy, name='privacy'),
    url(r'^terms$', terms, name='terms'),
    url(r'^faq$', faq, name='faq'),
    url(r'^career$', career, name='career'),
    url(r'^disclaimer$', disclaimer, name='disclaimer'),
    url(r'^acknowledge$', acknowledge, name='acknowledge'),

    url(r'^admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)