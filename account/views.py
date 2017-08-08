from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpForm
from  kutiva.views import index


def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('screencasts')
        else:
            return HttpResponse("Invalid login details supplied.")



    else:
        return render(request, 'account/signin.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('screencasts')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})
