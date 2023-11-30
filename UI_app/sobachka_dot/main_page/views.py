from django.shortcuts import render
from django.http import HttpResponse
from .models import Breed

def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return render(request, 'main_page/about.html')


def breed_map(request):
    return render(request, 'main_page/breed_map.html')


def breed_card(request):
    return render(request, 'main_page/breed_card.html')


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
# def forum(request):
#     return render(request, 'main_page/forum.html')
#
#
# def authorization(request):
#     return render(request, 'main_page/authorization.html')
