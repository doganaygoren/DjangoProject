from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#################################################################################

#PLACE APPLICATION VIEWS

#################################################################################

def places(request):

	return HttpResponse("This is places page")