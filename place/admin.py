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

	list_display=['title', 'status','parent','image_tag']
	list_filter=['status','created_at']
	readonly_fields=('image_tag',)

class PlaceAdmin(admin.ModelAdmin):

	list_display=['title','status','image_tag','category']
	list_filter=['status','created_at','category']
	inlines=[PlaceImageInline]
	readonly_fields=('image_tag',)

class ImageAdmin(admin.ModelAdmin):
	list_display=['title', 'place', 'image_tag']
	readonly_fields=('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Images, ImageAdmin)