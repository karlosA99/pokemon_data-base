"""pokemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pokemonApp import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vi.index, name="index"),
    path('citizen/', vi.CitizenList.as_view(), name='citizen'),
    path('trainer/', vi.TrainerList.as_view(), name='trainer'),
    path('pokemon/', vi.PokemonList.as_view(), name='pokemon'),
    path('caught_pokemon/', vi.CaughtPokemonList.as_view(), name='caught_pokemon'),
    path('community/', vi.Community.as_view(), name='community'),
    path('element/', vi.ElementList.as_view(), name='element'),
    path('region/', vi.RegionList.as_view(), name='region'),
    path('gym/', vi.GymList.as_view(), name='gym'),
    path('motion/', vi.MotionList.as_view(), name='motion'),
    path('species/', vi.SpeciesList.as_view(), name='species'),
    path('duel/', vi.DuelList.as_view(), name='duel'),
    path('about/', vi.AboutList.as_view(), name='about'),
    path('relevant/', vi.RelevantList.as_view(), name='relevant'),
    path('porcentage/', vi.Query1.as_view(), name='porcentage'),
    path('pokdetails/', vi.Query2.as_view(), name='pokdetails'),
    path('pokelevels/', vi.Query3.as_view(), name='pokelevels'),
    path('league/', vi.Query4.as_view(), name='league'),
    path('winners/', vi.Query5.as_view(), name='winners'),
    path('topmotions/', vi.Query6.as_view(), name='topmotions'),

]
