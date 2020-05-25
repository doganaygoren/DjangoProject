from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import UserProfile
from place.models import Category, Comment, Place
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
	return HttpResponseRedirect("/user/profile")

@login_required(login_url='/login')
def profile(request):

	current_user=request.user
	profile= UserProfile.objects.get(user_id=current_user.id)
	categories=Category.objects.all()
	comments=Comment.objects.filter(user_id=current_user.id)
	content={ 'profile':profile, 'categories':categories, 'comments':comments,}
	return render(request, 'profile.html',content)

@login_required(login_url='/login')
def profile_edit(request):

	if request.method=='POST':
		user_form=UserUpdateForm(request.POST, instance=request.user)
		profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,"Profile Updated Successfully.")
			return HttpResponseRedirect('/user/profile')
		else:
			messages.warning(request,form.errors)
			return HttpResponseRedirect('/user/profile_edit')
	else:
		categories=Category.objects.all()
		current_user=request.user
		user_form=UserUpdateForm(instance=request.user)
		profile_form=ProfileUpdateForm(instance=request.user.userprofile)
		profile=UserProfile.objects.get(user_id=current_user.id)
		content={'categories':categories, 'profile':profile, 'profile_form':profile_form }
		return render(request, 'profile_edit.html', content)


@login_required(login_url='/login')
def change_password(request):

	if request.method=='POST':
		form=PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,"Password changed successfully.")
			return HttpResponseRedirect('/user/change_password')
		else:
			messages.warning(request, "Please Correct the Error Below. <br>" + str(form.errors))
			return HttpResponseRedirect('/user/change_password')
	else:
		categories=Category.objects.all()
		form=PasswordChangeForm(request.user)
		content={'form':form, 'categories':categories}
		return render(request, 'password_change.html', content)


@login_required(login_url='/login')
def user_comments(request):

	categories=Category.objects.all()
	current_user=request.user
	comments=Comment.objects.filter(user_id=current_user.id)
	content={'categories':categories, 'comments':comments, }
	return render(request, 'profile.html', content)


@login_required(login_url='/login')
def deletecomment(request,id):

	current_user=request.user
	Comment.objects.filter(id=id, user_id=current_user.id).delete()
	messages.success(request, "Comment deleted successfully")
	return HttpResponseRedirect('/user/profile')