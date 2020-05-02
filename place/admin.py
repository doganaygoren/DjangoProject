from django.contrib import admin
from place.models import Category, Place,Images
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import format_html
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

	list_display=['title','category','image_tag','status']
	list_filter=['status','created_at','category']
	inlines=[PlaceImageInline]
	readonly_fields=('image_tag',)

class ImageAdmin(admin.ModelAdmin):
	list_display=['title', 'place', 'image_tag']
	readonly_fields=('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
	
	mptt_indent_field="title"
	list_display=('tree_actions', 'indented_title', 'related_places_count', 
		'related_places_cumulative_count')
	list_display_links=('indented_title',)

	def get_queryset(self, request):
		qs= super().get_queryset(request)

		qs=Category.objects.add_related_count(
			qs,
			Place,
			'category',
			'places_cumulative_count',
			cumulative=True)

		qs=Category.objects.add_related_count(
			qs,
			Place,
			'category',
			'places_count',
			cumulative=False)

		return qs

	def related_places_count(self, instance):
		return instance.places_count
	related_places_count.short_description='Related Places (For This Category)'

	def related_places_cumulative_count(self, instance):
		return instance.places_cumulative_count
	related_places_cumulative_count.short_description='Related Places(In Tree)'

admin.site.register(Category, CategoryAdmin2)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Images, ImageAdmin)





