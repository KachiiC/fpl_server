# Generated by Django 3.2.13 on 2022-05-21 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('matchday', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(38)])),
                ('name', models.CharField(max_length=150)),
                ('player_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MatchDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bench_points', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('gameweek', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(38)])),
                ('game_week_points', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('player_id', models.IntegerField()),
                ('points_total', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('team_value', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2000)])),
                ('transfers', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)])),
                ('transfers_cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_gameweek', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(38)])),
                ('last_gameweek_points', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('player_name', models.CharField(max_length=150)),
                ('player_id', models.IntegerField()),
                ('points_on_transfers', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('points_total', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3000)])),
                ('team_name', models.CharField(max_length=150)),
                ('team_value', models.IntegerField(validators=[django.core.validators.MinValueValidator(500), django.core.validators.MaxValueValidator(3000)])),
                ('transfers_total', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(570)])),
                ('chips', models.ManyToManyField(blank=True, to='fpl_players.Chip')),
                ('matches', models.ManyToManyField(blank=True, to='fpl_players.MatchDay')),
            ],
        ),
    ]
