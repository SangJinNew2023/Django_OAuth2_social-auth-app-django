from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_or_signup(request):
    return render(request, 'login_or_signup.html')

def login_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('App_auth:home'))
        else:
            createUser = User(username=email)
            createUser.set_password(password)
            createUser.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('App_auth:home'))

        return HttpResponseRedirect(reverse('App_auth:login-signup'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_auth:login-or-signup'))