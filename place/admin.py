from django.contrib import admin

from place.models import Category, Place,Images
# Register your models here.


############################################################################################

#ADMIN FIELDS WHICH ARE CREATED IN MODELS ARE DEFINED HERE

############################################################################################

class PlaceImageInline(admin.TabularInline):
	model= Images
	extra= 5


class CategoryAdmin(admin.ModelAdmin):

	list_display=['title', 'status','parent','image']
	list_filter=['status','created_at']

class PlaceAdmin(admin.ModelAdmin):

	list_display=['title','status','image','category']
	list_filter=['status','created_at','category']
	inlines=[PlaceImageInline]

class ImageAdmin(admin.ModelAdmin):
	list_display=['title', 'place', 'image']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Images, ImageAdmin)