from django.shortcuts import render
from django.http import HttpResponse
from .models import Breed

def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return render(request, 'main_page/about.html')


def breed_map(request):
    breeds = Breed.objects.all()
    return render(request, 'main_page/breed_map.html', {'breeds': breeds})


def breed_card(request):
    breed = Breed.objects.get(name='african')
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
#
#
# def authorization(request):
#     return render(request, 'main_page/authorization.html')
