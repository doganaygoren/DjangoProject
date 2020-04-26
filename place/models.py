from django.db import models

# Create your models here.


###########################################################################################

#PLACES DATABASE TABLE

###########################################################################################

class Category(models.Model):

	STATUS=(

		('True','Active'),
		('False','Inactive'),
	)
	title= models.CharField(max_length=100)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(blank=True,upload_to='images/')
	status=models.CharField(max_length=10, choices=STATUS)
	slug=models.SlugField()

	parent=models.ForeignKey('self',blank=True,null=True,related_name='children', on_delete=models.CASCADE)

	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Place(models.Model):

	STATUS=(

		('True', 'Active'),
		('False', 'Inactive')
	)
	
	category=models.ForeignKey(Category, on_delete=models.CASCADE) #Relationship with Category Table
	title=models.CharField(max_length=150)
	keywords=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	image=models.ImageField(blank=True, upload_to='images/')
	detail=models.TextField()
	status=models.CharField(max_length=25,choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Images(models.Model):
	place=models.ForeignKey(Place,on_delete=models.CASCADE)
	title=models.CharField(max_length=50,blank=True)
	image=models.ImageField(blank=True, upload_to='images/')

	def __str__(self):
		return self.title


		
