from django.shortcuts import render
from django.http import HttpResponse
from home.models import Setting

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	setting= Setting.objects.get(pk=1)
	content= {'setting': setting }
	return render(request, 'index.html', content)