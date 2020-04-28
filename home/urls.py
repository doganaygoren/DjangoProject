
#####################################################

#HOME APPLICATION URLS


######################################################

from django.urls import path

from . import views

urlpatterns=[
	
	# ex: /home/
	path('',views.index,name="index"),
	# ex: /about/
	path('about', views.about, name="about"),
	# ex: /contact/
	path('contact', views.contact, name="contact"),
]