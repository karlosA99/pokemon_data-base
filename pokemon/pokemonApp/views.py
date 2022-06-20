from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import ListView
from pokemonApp.models import *
from pokemonApp.tools import check_int_integrity


def index(request):
    return render(request, 'home/index.html')

class CitizenList(ListView):
    model = Citizen
    template_name = 'citizen/citizen.html'

    def get(self, request : HttpRequest) -> HttpResponse:
        citizen = Citizen.objects.all()

        if "name" in request.GET and request.GET["name"] != '':
            citizen = citizen.filter(name=request.GET(["name"]))
        if "age" in request.GET and request.GET["age"] != '' and check_int_integrity(request.GET["age"], 'int'):
            citizen = citizen.filter(age= int(request.GET["age"]))
        if "gender" in request.GET and request.GET["gender"] != '':
            citizen = citizen.filter(sex= request.GET["gender"])
        if "region" in request.GET and request.GET["region"] !='':
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

    def get(self, request : HttpRequest)-> HttpResponse:
        pokemons = Pokemon.objects.all()
        is_shiny = None
        if 'height' in request.GET and request.GET['height'] != '' and check_int_integrity(request.GET["height"], 'decimal'):
            pokemons = pokemons.filter(height= request.GET['height'])
        if 'weight' in request.GET and request.GET['weight'] != '' and check_int_integrity(request.GET["weight"], 'decimal'):
            pokemons = pokemons.filter(weight= request.GET['weight'])
        if 'nature' in request.GET and request.GET['nature'] != '':
            pokemons = pokemons.filter(nature= request.GET['nature'])
        if 'species' in request.GET and request.GET['species'] != '':
            pokemons = pokemons.filter(species_name__name= request.GET['species'])
        if 'gender' in request.GET and request.GET['gender'] != '':
            pokemons = pokemons.filter(sex= request.GET['gender'])
        if 'shiny' in request.GET and request.GET['shiny'] != '':
            if request.GET['shiny'] == 'No':
                is_shiny = False
            elif request.GET['shiny'] == 'Yes':
                is_shiny = True
            pokemons = pokemons.filter(shine= is_shiny)

        return render(request,self.template_name, {'object_list': pokemons})

class CaughtPokemonList(ListView):
    model = CaughtPokemon
    template_name = 'caught_pokemon/caught_pokemon.html'

    def get(self, request : HttpRequest)-> HttpResponse:
        caughtPokemons = CaughtPokemon.objects.all()

        if 'trainer' in request.GET and request.GET['trainer'] != '':
            caughtPokemons = caughtPokemons.filter(id_Trainer__name=request.GET['trainer'])
        if 'pokeball' in request.GET and request.GET['pokeball'] != '':
            caughtPokemons = caughtPokemons.filter(pokeball=request.GET['pokeball'])
        if 'caught_level' in request.GET and request.GET['caught_level'] != '' and check_int_integrity(request.GET["caught_level"], 'int'):
            caughtPokemons = caughtPokemons.filter(caught_level=int(request.GET['caught_level']))
        if 'actual_level' in request.GET and request.GET['actual_level'] and check_int_integrity(request.GET["actual_level"], 'int'):
            caughtPokemons = caughtPokemons.filter(actual_level=int(request.GET['actual_level']))

        return render(request,self.template_name, {'object_list': caughtPokemons})


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

    def get(self, request: HttpRequest)->HttpResponse:
        gym = Gym.objects.all()

        if 'gym_name' in request.GET and request.GET['gym_name'] != '':
            gym = gym.filter(name=request.GET['gym_name'])
        if 'element' in request.GET and request.GET['element'] != '':
            gym = gym.filter(element_name__name=request.GET['element'])

        return render(request,self.template_name, {'object_list' : gym})

class MotionList(ListView):
    model = Gym
    template_name = 'motion/motion.html'

    def get(self,request : HttpRequest)-> HttpResponse:
        motion = Motion.objects.all()

        if 'name' in request.GET and request.GET['name'] != '':
            motion = motion.filter(name=request.GET['name'])
        if 'element' in request.GET and request.GET['element'] != '':
            motion = motion.filter(element_name__name=request.GET['element'])

        return render(request,self.template_name, {'object_list' : motion})

class SpeciesList(ListView):
    model = Gym
    template_name = 'species/species.html'

    def get(self,request : HttpRequest)-> HttpResponse:
        species = Species.objects.all()


        is_legendary = None
        if 'name' in request.GET and request.GET['name'] != '':
            species = species.filter(name=request.GET['name'])
        if 'strong_element' in request.GET and request.GET['strong_element'] != '':
            species = species.filter(strong_element__name=request.GET['strong_element'])
        if 'secundary_element' in request.GET and request.GET['secundary_element'] != '':
            species = species.filter(secundary_element__name=request.GET['secundary_element'])
        if 'region' in request.GET and request.GET['region'] != '':
            species = species.filter(region__name=request.GET['region'])
        if 'legendary' in request.GET and request.GET['legendary'] != '':
            if request.GET['legendary'] == 'No':
                is_legendary = False
            elif request.GET['legendary'] == 'Yes':
                is_legendary = True
            species = species.filter(legendary= is_legendary)

        return render(request,self.template_name, {'object_list' : species})


class DuelList(ListView):
    model = Duel
    template_name = 'duel/duel.html'

    def get(self, request :HttpRequest)-> HttpResponse:
        duel = Duel.objects.all()

        if 'winner' in request.GET and request.GET['winner'] != '':
            duel = duel.filter(winner__name=request.GET['winner'])
        if 'region' in request.GET and request.GET['region'] != '':
            duel = duel.filter(region__name=request.GET['region'])

        return render(request,self.template_name, {'object_list' : duel})

class AboutList(ListView):

    model = About
    template_name = 'about/about.html'


class Query1(ListView):
    model = Trainer
    template_name = '' #!rellenar


    def get(self, request : HttpRequest)-> HttpResponse:
        porcentage = 0
        citizens = Citizen.objects.all()
        trainers = Trainer.objects.all()

        if 'region' in request.GET and request.GET['region'] != '':
            citizens_count = citizens.filter(born_region__name=request.GET["region"]).count()
            trainers = trainers.filter(born_region__name=request.GET["region"])
            count_citizen = citizens.count()
            count_trainers = trainers.count()
            if count_citizen > 0:
                porcentage = (count_trainers * 100) / count_citizen

        return render(request, self.template_name, {'object_list' : trainers,'porcentage' : porcentage})

class Query2(ListView):
    model = CaughtPokemon
    template_name = ''  #!rellenar

    def get(self,request : HttpRequest)-> HttpResponse:
        caught_pokemons = CaughtPokemon.objects.all()

        if 'trainer' in request.GET and request.GET['trainer'] != '':
            caught_pokemons = caught_pokemons.filter(id_Trainer__name=request.GET['trainer'])

        if 'element' in request.GEt and request.GET['trainer'] != '':
            caught_pokemons = caught_pokemons.filter(species_name__strong_element__name= request.GET['element'])

        return render(request,self.template_name,{'object_list' : caught_pokemons})
        #todo WAITING FOR TESTING

class Query3(ListView):
    model = CaughtPokemon
    template_name = ''  #!rellenar

    def get(self,request : HttpRequest)-> HttpResponse:
        caught_pokemons = CaughtPokemon.objects.all()

        if 'qtrainer' in request.GET and request.GET['qtrainer'] != '':
            caught_pokemons = caught_pokemons.filter(id_Trainer__name=request.GET['qtrainer'])

        if 'qspecies' in request.GET and request.GET['qspecies'] !='':
            caught_pokemons = caught_pokemons.filter(species_name=request.GET['qspecies']).order_by('actual_level')


        return render(request,self.template_name, {'caught_pokemons' : caught_pokemons})


