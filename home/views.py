from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

################################################################################

#HOME APPLICATION VIEWS

################################################################################

def index(request):

	text="Doganay Goren"
	context={'text': text}
	return render(request, 'index.html',context)