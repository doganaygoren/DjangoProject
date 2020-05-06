from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import UserProfile

# Create your views here.

def index(request):
	return HttpResponse("User Page")

def profile(request):

	current_user=request.user
	profile= UserProfile.objects.get(user_id=current_user.id)
	content={ 'profile':profile,  }

	return render(request, 'profile.html',content)