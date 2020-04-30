from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Setting, ContactFormMessage, ContactForm
from place.models import Place, Category
from django.contrib import messages

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	setting= Setting.objects.get(pk=1)
	slider= Place.objects.all().order_by('-id')[:3]
	categories=Category.objects.all()

	content= {'setting': setting, 'page': 'home', 'slider':slider, 'categories':categories }
	return render(request, 'index.html', content)

def about(request):

	about= Setting.objects.get(pk=1)
	content= {'about': about, 'page':'about' }
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
	content={'contact':contact, 'page':'contact'}
	return render(request, 'contact.html', content)