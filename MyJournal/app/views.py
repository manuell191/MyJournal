from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm, PostForm, UpdateForm
from .models import Profile, Post


# Create your views here.
def index(request):
	return redirect('login')

def userLogin(request):
	if request.user.is_authenticated:
		return redirect('post')

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('load')

			messages.error(request, 'Username OR password is incorrect')

	context = {'form': LoginForm}
	return render(request, 'login.html', context)

def signup(request):
	if request.user.is_authenticated:
		return redirect('post')

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			if password1 != password2:
				messages.error(request, 'Passwords do not match')
			else:
				User.objects.create_user(username=username, password=password1)
				user = User.objects.get(username=username)
				userId = user.id
				profile = Profile(user=user)
				profile.save()

				user = authenticate(request, username=username, password=password1)
				login(request, user)
				return redirect('load')
	context = {'form': SignupForm}
	return render(request, 'signup.html', context)

def load(request):
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'load.html')

def createPost(request):
	if not request.user.is_authenticated:
		return redirect('login')

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			content = request.POST.get('content')
			profile = Profile.objects.get(user=request.user)
			post = Post(content=content, author=profile)
			post.save()
			return redirect('view')

	context = {'form': PostForm}

	return render(request, 'createPost.html', context)

def viewPost(request):
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'viewPost.html')