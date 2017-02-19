"""csesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from csesite.views import hello,time,timeahead
from cses.views import faculty,mainfaculty,sendmail,send_email,contact,index,research,event,aboutus,course,lab,acad,student,chat,chatroot,thanks,student
from csesite.settings import *
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$',time),
    url(r'^timeahead/(\d{1,2})/$',timeahead),
    url(r'^eachfaculty/(\d{1,2})/$',faculty),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^faculty/$',mainfaculty),
    url(r'^sendmail/$',sendmail),
    url(r'^send_email/$',send_email),
    url(r'^contact/$', contact),
    url(r'^home/$',index),
    url(r'^$',index),
    url(r'^research/$',research),
    url(r'^events/$',event),
    url(r'^aboutus/$',aboutus),
    url(r'^course/$',course),
    url(r'^lab/$',lab),
    url(r'^programmes/$',acad),
    url(r'^student/$', student),
    url(r'^chat/$', chat),
    url(r'^chatroot/$',chatroot),
    url(r'^contact/thanks$',thanks),
    url(r'^students$',student),
    



]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)


