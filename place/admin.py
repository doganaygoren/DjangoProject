from django.contrib import admin

from place.models import Category, Place
# Register your models here.


############################################################################################

#ADMIN FIELDS WHICH ARE CREATED IN MODELS ARE DEFINED HERE

############################################################################################

class CategoryAdmin(admin.ModelAdmin):

	list_display=['title', 'status','parent','image']
	list_filter=['status','created_at']

class PlaceAdmin(admin.ModelAdmin):

	list_display=['title','status','image','category']
	list_filter=['status','created_at','category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)