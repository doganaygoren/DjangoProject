from django.shortcuts import render
from django.http import HttpResponse
from home.models import Setting

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	setting= Setting.objects.get(pk=1)
	content= {'setting': setting, 'page': 'home' }
	return render(request, 'index.html', content)

def about(request):

	about= Setting.objects.get(pk=1)
	content= {'about': about, 'page':'about' }
	return render(request, 'about.html', content)

def contact(request):

	contact=Setting.objects.get(pk=1)
	content={'contact':contact, 'page':'contact'}
	return render(request, 'contact.html', content)