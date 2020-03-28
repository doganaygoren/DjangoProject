####################################################################

#PLACE APPLICATION URLS

####################################################################

from django.urls import path

from . import views

urlpatterns=[
	
	# ex: /places/
	path('',views.places,name="places"),
]