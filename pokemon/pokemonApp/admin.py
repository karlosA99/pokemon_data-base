from django.contrib import admin
from pokemonApp.models import CaughtPokemon, Citizen, City, Community, Duel, Element, Gym, Motion, Pokemon, Region, Species, Trainer, Village

# Register your models here.

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Element)
admin.site.register(Community)
admin.site.register(Village)
admin.site.register(Citizen)
admin.site.register(Gym)
admin.site.register(Motion)
admin.site.register(Trainer)
admin.site.register(Species)
admin.site.register(Pokemon)
admin.site.register(CaughtPokemon)
admin.site.register(Duel)