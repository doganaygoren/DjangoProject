from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

############################################################################################################

#Home FRONTEND MODELS

###########################################################################################################

class Setting(models.Model):

	STATUS=(

		('True','Active'),
		('False','Inactive'),
	)

	title=models.CharField(max_length=150)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	company=models.CharField(max_length=50)
	address=models.CharField(max_length=255)
	phone=models.CharField(max_length=25)
	fax=models.CharField(max_length=25)
	email=models.CharField(max_length=50)
	smtpserver=models.CharField(max_length=50)
	smtpemail=models.CharField(max_length=50)
	smtppassword=models.CharField(max_length=50)
	smtpport=models.CharField(max_length=5)
	icon=models.ImageField(blank=True, upload_to='images/')
	facebook=models.CharField(max_length=50)
	instagram=models.CharField(max_length=50)
	twitter=models.CharField(max_length=50)
	aboutus=RichTextUploadingField()
	contact=RichTextUploadingField()
	status=models.CharField(max_length=10, choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
