from django.urls import path
from . import views
####################################################################

#PLACE APPLICATION URLS

####################################################################

urlpatterns=[

	# ex: /user/
	path('',views.index,name="index"),
	# ex:/profile
	path('profile', views.profile, name="profile")
]