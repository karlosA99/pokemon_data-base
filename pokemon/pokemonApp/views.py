from django.db import reset_queries
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import ListView
from pokemonApp.models import *


def index(request):
    return render(request, 'home/index.html')
    
class CitizenList(ListView):
    model = Citizen
    template_name = 'citizen/citizen.html'

    def get(self, request : HttpRequest) -> HttpResponse:
        citizen = Citizen.objects.all()

        if "name" in request.GET and request.GET["name"] != '':
            citizen = citizen.filter(name=request.GET(["name"]))
        if "age" in request.GET and request.GET["age"] != '':
            citizen = citizen.filter(age= int(request.GET["age"]))
        if "gender" in request.GET and request.GET["gender"] != '':
            citizen = citizen.filter(sex= request.GET["gender"])
        if "region" in request.GET and request.GET['region'] !='':
            citizen = citizen.filter(born_region__name=request.GET["region"])

        return render(request, self.template_name, {'object_list': citizen})
class TrainerList(ListView):
    model = Trainer
    template_name = 'trainer/trainer.html'

    def get(self, request : HttpRequest)-> HttpResponse:
        trainer = Trainer.objects.all()
        if 'gym_name' in request.GET and request.GET['gym_name'] != '':
            trainer = trainer.filter(id_Gym__name=request.GET['gym_name'])

        return render(request, self.template_name, {'object_list' : trainer})

class PokemonList(ListView):
    model = Pokemon
    template_name = 'pokemon/pokemon.html'

    # def get(self, request : HttpRequest)-> HttpResponse:
    #     pokemons = Pokemon.objects.all()

    #     if 'height' in request.GET and request.GET['height'] != '':
    #         pokemons = pokemns.filter(height= request.GET['height'])
    #     if 'weight' in request.GET and request.GET['weight'] != '':
    #         pokemnos = pokemns.filter(weight= request.GET['weight'])
    #     if 'nature' in request.GET and request.GET['nature'] != '':
    #         pokemns = pokemns.filter(nature= request.GET['nature'])
    #     if 'species' in request.GET and request.GET['species'] != '':
    #         pokemns = pokemns.filter(species__name= request.GET['species'])
    #     if 'gender' in request.GET and request.GET['gender'] != '':
    #         pokemns = pokemns.filter(sex= request.GET['gender'])
    #     if 'is_shiny' in request.GET and request.GET['is_shiny'] != '':
    #         pokemns = pokemns.filter(shine= request.GET['is_shiny'])
    #//

class CaughtPokemonList(ListView):
    model = CaughtPokemon
    template_name = 'caught_pokemon/caught_pokemon.html'

class Community(ListView):
    model = Community
    template_name = 'community/community.html'

class ElementList(ListView):
    model = Element
    template_name = 'element/element.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        elements = Element.objects.all()

        if "name" in request.GET and request.GET["name"] != '':
            elements = elements.filter(name = request.GET["name"])

        return render(request,self.template_name, {'object_list':elements})

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