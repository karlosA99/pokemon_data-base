from django.db import models

# Create your models here.

class Region(models.Model):
    id_Region = models.IntegerField(primary_key= True) #id_regon = coder_region
    name = models.CharField(max_length = 30)

class Community(models.Model):
    id_Community = models.IntegerField(primary_key= True)
    id_Region = models.ForeignKey(Region, null= False,on_delete= models.RESTRICT)

class City(models.Model):
    id_City = models.OneToOneField(Community,primary_key= True, on_delete= models.CASCADE)

class Gym(models.Model):
    id_Gym = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 30)
    element_name = models.CharField(max_length= 15)
    id_City = models.ForeignKey(City,null= False,on_delete= models.CASCADE) #DUDA

class Citizen(models.Model):
    id_Citizen = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 30)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length= 1)
    id_City = models.ForeignKey(City, null= False,on_delete= models.CASCADE)

class Element(models.Model):
    name = models.CharField(primary_key= True , max_length= 30)

class Village(models.Model):
    id_village = models.OneToOneField(Community, primary_key= True,on_delete= models.CASCADE)

class Species(models.Model):
    name = models.CharField(primary_key= True, max_length= 30)
    legendary = models.BooleanField()

class Motion(models.Model):
    name = models.CharField(primary_key= True, max_length= 15)
    element_name = models.ForeignKey(Element, null= False, on_delete= models.CASCADE)

class Trainer(models.Model):
    id_Trainer = models.ForeignKey(Citizen, on_delete= models.CASCADE)
    id_Gym = models.ForeignKey(Gym, null= True, on_delete= models.CASCADE)
    class Meta:
        unique_together = [['id_Trainer','id_Gym']]

class Pokemon(models.Model):
    id_Pokemon = models.IntegerField(primary_key= True)
    height = models.DecimalField(decimal_places=2, max_digits= 7)
    shine = models.BooleanField()
    sex = models.CharField(max_length= 1)
    weight = models.DecimalField(decimal_places=2, max_digits= 7)
    nature = models.CharField(max_length= 15)
    id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)
    species_name = models.ForeignKey(Species, on_delete= models.CASCADE)

class CaughtPokemon(models.Model):
    id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)
    id_Pokemon = models.ForeignKey(Pokemon, on_delete= models.CASCADE)
    nickname = models.CharField(max_length= 15)
    pokeball = models.CharField(max_length= 15)
    caught_level = models.IntegerField()
    actual_level = models.IntegerField()
    class Meta:
        unique_together = [['id_Trainer','id_Pokemon']]

#!duda si los foraneos q son primarios pueden tener nulos.

class Gym_Trainer(models.Model):
    id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)
    id_Gym = models.ForeignKey(Gym, on_delete= models.CASCADE)
    class Meta:
        unique_together = [['id_Trainer','id_Gym']]

class Species_Region(models.Model):
    name_species = models.ForeignKey(Species, on_delete= models.CASCADE)
    id_Region = models.ForeignKey(Region, on_delete= models.CASCADE)
    class Meta:
        unique_together = [['name_species','id_Region']]

class Species_Motion(models.Model):
    name_species = models.ForeignKey(Species, on_delete= models.CASCADE)
    name_motion = models.ForeignKey(Motion, on_delete= models.CASCADE)
    class Meta:
        unique_together = [['name_species','name_motion']]

class Species_Element(models.Model):
    name_species = models.ForeignKey(Species, on_delete= models.CASCADE)
    name_element = models.ForeignKey(Element, on_delete= models.CASCADE)
    class Meta:
        unique_together = [['name_species','name_element']]


class Caught_Pokemon_Motion(models.Model):
    name_motion = models.ForeignKey(Motion, on_delete= models.CASCADE)
    id_Pokemon = models.ForeignKey(Pokemon, on_delete= models.CASCADE)
    id_Trainer = models.ForeignKey(Trainer, on_delete= models.CASCADE)

    class Meta:
        unique_together = [['name_motion','id_Pokemon','id_Trainer']]
#!falta la tabla de duelo y la tabla de pokemon capturado con duelo








