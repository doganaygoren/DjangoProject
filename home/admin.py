from django.contrib import admin
from home.models import Setting, ContactFormMessage, UserProfile

# Register your models here.

##############################################################################################

#REGISTER MODELS WHICH ARE CREATED IN MODELS.PY

##############################################################################################

class ContactFormAdmin(admin.ModelAdmin):

	list_display=['name','subject','status', 'created_at']
	list_filter=['status','created_at']


class UserProfileAdmin(admin.ModelAdmin):

	list_display=['user_name','phone','city', 'country' ,'image_tag']




admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)