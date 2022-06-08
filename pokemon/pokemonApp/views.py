from operator import index
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView
from pokemonApp.models import *

def index(request):
    return render(request, 'home/index.html')
class CitizenList(ListView):
    model = Citizen
    template_name = 'citizen/citizen.html'

class TrainerList(ListView):
    model = Trainer
    template_name = 'trainer/trainer.html'

class PokemonesList(ListView):
    model = Pokemon
    template_name = 'pokemones/pokemones.html'

class CaughtPokemonList(ListView):
    model = CaughtPokemon
    template_name = 'caught_pokemon/caught_pokemon.html'

class Community(ListView):
    model = Community
    template_name = 'community/community.html'
