from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about),
    path('breed-map', views.breed_map),
    path('breed-card', views.breed_card),
    path('dog-card', views.dog_card),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    path('registration-page', views.registration, name='registration'),
    # path('personal-area', views.personal_area),
    # path('faq', views.questions),
    # path('forum', views.forum),
]

