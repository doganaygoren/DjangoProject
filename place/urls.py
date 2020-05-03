from django.urls import path
from . import views
####################################################################

#PLACE APPLICATION URLS

####################################################################

urlpatterns=[

	# ex: /place/
	path('',views.index,name="index"),
	# ex: place/comment/1
	path('comment/<int:id>',views.placeComment,name="placeComment"),
	
]