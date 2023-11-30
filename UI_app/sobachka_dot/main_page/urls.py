from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('breed-map', views.breed_map),
    path('breed-card', views.breed_card),
    path('dog-card', views.dog_card),
    # path('personal-area', views.personal_area),
    # path('faq', views.questions),
    # path('forum', views.forum),
    # path('authorization-page', views.authorization),
]