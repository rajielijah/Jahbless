from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
def signup(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password=password)
			login (request, User)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})