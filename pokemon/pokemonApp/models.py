from django.db import models
from django.utils import timezone as tz


# Create your models here.


class Element(models.Model):
    name = models.CharField(primary_key= True , max_length= 30)
    strong_vs = models.ManyToManyField('self',blank= True)

#?Related with Region
class Region(models.Model):
    id_Region = models.IntegerField(primary_key= True) #id_regon = region_code
    name = models.CharField(max_length = 30)

class Community(models.Model):
    id_Community = models.IntegerField(primary_key= True)
    id_Region = models.ForeignKey(Region, null= False,on_delete= models.RESTRICT)

class City(models.Model):
    id_City = models.OneToOneField(Community,primary_key= True, on_delete= models.CASCADE)
class Village(models.Model):
    id_village = models.OneToOneField(Community, primary_key= True,on_delete= models.CASCADE)

class Citizen(models.Model):
    id_Citizen = models.CharField(primary_key= True,max_length= 10)
    name = models.CharField(max_length= 30)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length= 1)
    #AQUI ES ID COMMUNITY
    id_City = models.ForeignKey(City,on_delete= models.CASCADE)
    born_region = models.ForeignKey(Region,on_delete= models.CASCADE)

class Gym(models.Model):
    id_Gym = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 30)
    element_name = models.ForeignKey(Element, on_delete= models.CASCADE)
    id_City = models.OneToOneField(City,on_delete= models.CASCADE)
    leader = models.OneToOneField(Citizen,on_delete= models.RESTRICT)

class Motion(models.Model):
    name = models.CharField(primary_key= True, max_length= 15)
    element_name = models.ForeignKey(Element, null= False, on_delete= models.CASCADE)

class Trainer(Citizen):
    id_Trainer = models.CharField(unique=True, max_length= 30)
    id_Gym = models.ForeignKey(Gym, null= True, on_delete= models.SET_NULL,blank= True,related_name="%(class)s_id_Gym")
    oponent = models.ManyToManyField('self',through='Duel',through_fields=['trainer1', 'trainer1'])# preguntar esto al chuchy
    medlas = models.ManyToManyField(Gym, blank= True,related_name= "%(class)s_medals")

class Species(models.Model):
    id_species = models.AutoField(primary_key= True)
    strong_element = models.ForeignKey(Element,on_delete= models.CASCADE,related_name= "%(class)s_strong_element")
    secundary_element = models.ForeignKey(Element,on_delete= models.CASCADE,related_name= "%(class)s_secundary_element")
    name = models.CharField(max_length= 30)
    legendary = models.BooleanField()
    natural_motion = models.ManyToManyField(Motion,related_name="%(class)s_natural_motion")
    taught_motion = models.ManyToManyField(Motion,related_name= "%(class)s_taught_motion")
    region = models.ManyToManyField(Region)

class Pokemon(models.Model):
    id_Pokemon = models.AutoField(primary_key= True)
    height = models.DecimalField(decimal_places=2, max_digits= 7)
    shine = models.BooleanField()
    sex = models.CharField(max_length= 1)
    weight = models.DecimalField(decimal_places=2, max_digits= 7)
    nature = models.CharField(max_length= 15)
    species_name = models.ForeignKey(Species, on_delete= models.CASCADE)

class CaughtPokemon(Pokemon):
    id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)
    nickname = models.CharField(max_length= 15)
    pokeball = models.CharField(max_length= 15)
    caught_level = models.IntegerField(default=1) #esto no deberia ser asi, deberia averiguar q bola con l on-off value
    actual_level = models.IntegerField(default=1)
    motion = models.ManyToManyField(Motion)
    # class Meta:
    #     unique_together = [['id_Trainer','id_Pokemon']]
class Duel(models.Model):
    trainer1 = models.ForeignKey(Trainer,on_delete= models.CASCADE,related_name= "%(class)s_trainer1")
    trainer2 = models.ForeignKey(Trainer,on_delete= models.CASCADE,related_name= "%(class)s_trainer2")
    date = models.DateTimeField(auto_now_add=True)
    region = models.ForeignKey(Region,on_delete= models.CASCADE)
    winner = models.ForeignKey(Trainer, on_delete= models.CASCADE)
    pokemons_played = models.ManyToManyField(CaughtPokemon)


# class Gym_Trainer(models.Model):
#     id_Trainer = models.ForeignKey(Trainer, primary_key= True, on_delete= models.CASCADE)
#     id_Gym = models.ForeignKey(Gym, on_delete= models.CASCADE)
#     class Meta:
#         unique_together = [['id_Trainer','id_Gym']]

# class Species_Region(models.Model):
#     name_species = models.ForeignKey(Species, primary_key= True, on_delete= models.CASCADE)
#     id_Region = models.ForeignKey(Region, on_delete= models.CASCADE)
#     class Meta:
#         unique_together = [['name_species','id_Region']]

# class Species_Motion(models.Model):
#     name_species = models.ForeignKey(Species, primary_key= True, on_delete= models.CASCADE)
#     name_motion = models.ForeignKey(Motion, on_delete= models.CASCADE)
#     class Meta:
#         unique_together = [['name_species','name_motion']]

# class Species_Element(models.Model):
#     name_species = models.ForeignKey(Species, primary_key= True, on_delete= models.CASCADE)
#     name_element = models.ForeignKey(Element, on_delete= models.CASCADE)
#     class Meta:
#         unique_together = [['name_species','name_element']]


# class Caught_Pokemon_Motion(models.Model):
#     name_motion = models.ForeignKey(Motion, on_delete= models.CASCADE)
#     id_Pokemon = models.ForeignKey(Pokemon, primary_key= True, on_delete= models.CASCADE)
#     id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)

#     class Meta:
#         unique_together = [['name_motion','id_Pokemon','id_Trainer']]








