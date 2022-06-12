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

class PokemonList(ListView):
    model = Pokemon
    template_name = 'pokemon/pokemon.html'

class CaughtPokemonList(ListView):
    model = CaughtPokemon
    template_name = 'caught_pokemon/caught_pokemon.html'

class Community(ListView):
    model = Community
    template_name = 'community/community.html'

class ElementList(ListView):
    model = Element
    template_name = 'element/element.html'
    
class RegionList(ListView):
    model = Region
    template_name = 'region/region.html'

class GymList(ListView):
    model = Gym
    template_name = 'gym/gym.html'
    
class MotionList(ListView):
    model = Gym
    template_name = 'motion/motion.html'

class SpeciesList(ListView):
    model = Gym
    template_name = 'species/species.html'

class DuelList(ListView):
    model = Duel
    template_name = 'duel/duel.html'

class AboutList(ListView):
    model = About
    template_name = 'about/about.html'