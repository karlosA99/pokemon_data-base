# Generated by Django 3.2.7 on 2022-06-20 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id_Citizen', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.SmallIntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id_Community', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('strong_vs', models.ManyToManyField(blank=True, to='pokemonApp.Element')),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('name', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('element_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.element')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id_Pokemon', models.AutoField(primary_key=True, serialize=False)),
                ('height', models.DecimalField(decimal_places=2, max_digits=7)),
                ('shine', models.BooleanField()),
                ('sex', models.CharField(max_length=1)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('nature', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_Region', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Relevant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CaughtPokemon',
            fields=[
                ('pokemon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pokemonApp.pokemon')),
                ('nickname', models.CharField(max_length=15)),
                ('pokeball', models.CharField(max_length=15)),
                ('caught_level', models.IntegerField()),
                ('actual_level', models.IntegerField()),
            ],
            bases=('pokemonApp.pokemon',),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_City', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pokemonApp.community')),
            ],
        ),
        migrations.CreateModel(
            name='NaturalMotion',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pokemonApp.motion')),
            ],
        ),
        migrations.CreateModel(
            name='TaughtMotion',
            fields=[
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pokemonApp.motion')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id_village', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pokemonApp.community')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id_species', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('legendary', models.BooleanField()),
                ('motion', models.ManyToManyField(related_name='species_motion', to='pokemonApp.Motion')),
                ('region', models.ManyToManyField(to='pokemonApp.Region')),
                ('secundary_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_secundary_element', to='pokemonApp.element')),
                ('strong_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='species_strong_element', to='pokemonApp.element')),
                ('natural_motion', models.ManyToManyField(related_name='species_natural_motion', to='pokemonApp.NaturalMotion')),
                ('taught_motion', models.ManyToManyField(related_name='species_taught_motion', to='pokemonApp.TaughtMotion')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='species_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.species'),
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id_Gym', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('element_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.element')),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='pokemonApp.citizen')),
                ('id_City', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.city')),
            ],
        ),
        migrations.CreateModel(
            name='Duel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.region')),
                ('pokemons_played', models.ManyToManyField(to='pokemonApp.CaughtPokemon')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='id_Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pokemonApp.region'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='born_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.region'),
        ),
        migrations.AddField(
            model_name='citizen',
            name='id_Community',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.community'),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('citizen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pokemonApp.citizen')),
                ('id_Gym', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_id_Gym', to='pokemonApp.gym')),
                ('medals', models.ManyToManyField(blank=True, related_name='trainer_medals', to='pokemonApp.Gym')),
                ('oponent', models.ManyToManyField(related_name='_pokemonApp_trainer_oponent_+', through='pokemonApp.Duel', to='pokemonApp.Trainer')),
            ],
            bases=('pokemonApp.citizen',),
        ),
        migrations.AddField(
            model_name='duel',
            name='trainer1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duel_trainer1', to='pokemonApp.trainer'),
        ),
        migrations.AddField(
            model_name='duel',
            name='trainer2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duel_trainer2', to='pokemonApp.trainer'),
        ),
        migrations.AddField(
            model_name='duel',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.trainer'),
        ),
        migrations.AddField(
            model_name='caughtpokemon',
            name='id_Trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemonApp.trainer'),
        ),
        migrations.AddField(
            model_name='caughtpokemon',
            name='natural_motion',
            field=models.ManyToManyField(to='pokemonApp.NaturalMotion'),
        ),
        migrations.AddField(
            model_name='caughtpokemon',
            name='taught_motion',
            field=models.ManyToManyField(to='pokemonApp.TaughtMotion'),
        ),
    ]
