from django.contrib import admin
from home.models import Setting, ContactFormMessage

# Register your models here.

##############################################################################################

#REGISTER MODELS WHICH ARE CREATED IN MODELS.PY

##############################################################################################

class ContactFormAdmin(admin.ModelAdmin):

	list_display=['name','subject','status', 'created_at']
	list_filter=['status','created_at']




admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Setting)