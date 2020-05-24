from django.urls import path
from . import views
####################################################################

#PLACE APPLICATION URLS

####################################################################

urlpatterns=[

	# ex: /user/
	path('',views.index,name="index"),
	# ex:/user/profile
	path('profile', views.profile, name="profile"),
	# ex:/user/profile_edit
	path('profile_edit', views.profile_edit, name="profile_edit"),
	# ex:/user/change_password
	path('change_password', views.change_password, name="change_password"),
]