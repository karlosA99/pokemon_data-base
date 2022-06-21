# Generated by Django 3.2.7 on 2022-06-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonApp', '0005_naturalmotion_taughtmotion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relevant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='species',
            name='natural_motion',
            field=models.ManyToManyField(related_name='species_natural_motion', to='pokemonApp.NaturalMotion'),
        ),
        migrations.AlterField(
            model_name='species',
            name='taught_motion',
            field=models.ManyToManyField(related_name='species_taught_motion', to='pokemonApp.TaughtMotion'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='oponent',
            field=models.ManyToManyField(related_name='_pokemonApp_trainer_oponent_+', through='pokemonApp.Duel', to='pokemonApp.Trainer'),
        ),
    ]
