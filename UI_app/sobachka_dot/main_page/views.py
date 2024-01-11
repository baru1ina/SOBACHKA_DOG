from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Breed
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return render(request, 'main_page/about.html')


def breed_map(request):
    breeds = Breed.objects.all()
    return render(request, 'main_page/breed_map.html', {'breeds': breeds})


def breed_card(request):
    breed = Breed.objects.get(name='Affenpinscher')
    return render(request, 'main_page/breed_card.html', {'breed': breed})


def dog_card(request):
    return render(request, 'main_page/dog_card.html')




# def personal_area(request):
#     return render(request, 'main_page/personal_area.html')
#
#
# def questions(request):
#     return render(request, 'main_page/faq.html')
#
#


def forum(request):
    return render(request, 'main_page/forum.html')


@csrf_protect
def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("something went wrong, please try again."))
            return redirect('log_in')

    else:
        return render(request, 'main_page/log_in.html')


def log_out(request):
    logout(request)
    messages.success(request, ("your lovely doggies will be waiting for you to return!"))
    return redirect('index')


def registration(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("registration successful!"))
            return redirect('index')
    else:
        # form = UserCreationForm()
        form = RegisterUserForm()

    return render(request, 'main_page/registration.html', {'form': form})

