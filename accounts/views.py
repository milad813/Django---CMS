from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('my_app:blog_home')
            else:
                # messages.error(request,"unfortunately couldn't log you in, Username or password is incorrect")
                messages.add_message(request, messages.ERROR, "unfortunately couldn't log you in, Username or password is incorrect")
                print(dir(messages))
                return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('my_app:blog_home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('my_app:blog_home')
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect('my_app:blog_home')