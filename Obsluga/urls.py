from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokoje', views.pokoje, name='pokoje'),
    path('spa', views.spa, name='spa'),
    path('infopokoje', views.infopokoje, name='infopokoje'),
    path('infospa', views.infospa, name='infospa'),
    path('onas', views.onas, name='onas'),
    path('rejestruj', views.rejestruj, name='rejestruj'),
    path('zaloguj', views.zaloguj, name='zaloguj'),
    path('wyloguj', views.wyloguj, name='wyloguj'),
]
