from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactFormMessage, ContactForm
from place.models import Place, Category, Images, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	setting= Setting.objects.get(pk=1)
	slider= Place.objects.all().order_by('?')[:3]
	categories=Category.objects.all()
	checkOutPlaces=Place.objects.all()[:10]
	bestPlaces=Place.objects.all().order_by('?')[:4]

	content= {'setting': setting, 'page': 'home', 'slider':slider, 'categories':categories,
				'checkOutPlaces':checkOutPlaces, 'bestPlaces': bestPlaces }
	return render(request, 'index.html', content)

def about(request):

	about= Setting.objects.get(pk=1)
	categories=Category.objects.all()
	content= {'about': about, 'page':'about', 'categories':categories }
	return render(request, 'about.html', content)

def contact(request):


	if request.method== 'POST':

		form=ContactForm(request.POST)
		if form.is_valid():
			data=ContactFormMessage() #model connection
			data.name= form.cleaned_data['name']
			data.email= form.cleaned_data['email']
			data.subject= form.cleaned_data['subject']
			data.message= form.cleaned_data['message']
			data.ip= request.META.get('REMOTE_ADDR')
			messages.success(request, "Your message has been sent. Thank you!")
			data.save()
			return HttpResponseRedirect('/contact')

	contact=Setting.objects.get(pk=1)
	categories=Category.objects.all()
	content={'contact':contact, 'page':'contact', 'categories':categories}
	return render(request, 'contact.html', content)


def place(request):

	categories=Category.objects.all()
	places=Place.objects.all()
	content={'categories' : categories, 'places':places}
	return render(request, 'place.html', content)


def placeDetail(request,id,slug):

	place=Place.objects.get(id=id)
	gallery= Images.objects.filter(place_id=id)
	category=Category.objects.all()
	lastPlaces=Place.objects.all().order_by('-id')[:3]
	comments= Comment.objects.filter(place_id=id,status='True')
	content={'place':place, 'gallery':gallery, 'category':category, 'lastPlaces':lastPlaces, 'comments':comments}
	return render(request, 'place-detail.html', content)

