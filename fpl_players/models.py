# DJANGO MODELS
from django.db import models
# TOOLS
from tools.model_tools import max_min


class Chip(models.Model):
    date = models.DateTimeField()
    matchday = models.IntegerField(validators=max_min(0, 38))
    name = models.CharField(max_length=150)
    player_id = models.IntegerField()


class MatchDay(models.Model):
    bench_points = models.IntegerField(validators=max_min(0, 100))
    gameweek = models.IntegerField(validators=max_min(0, 38))
    game_week_points = models.IntegerField(validators=max_min(0, 300))
    player_id = models.IntegerField()
    points_total = models.IntegerField(validators=max_min(0, 300))
    team_value = models.IntegerField(validators=max_min(0, 2000))
    transfers = models.IntegerField(validators=max_min(0, 15))
    transfers_cost = models.IntegerField(validators=max_min(0, 100))


class Player(models.Model):
    chips = models.ManyToManyField('Chip', blank=True)
    current_gameweek = models.IntegerField(validators=max_min(1, 38))
    last_gameweek_points = models.IntegerField(validators=max_min(0, 300))
    matches = models.ManyToManyField('MatchDay', blank=True)
    player_name = models.CharField(max_length=150)
    player_id = models.IntegerField()
    points_on_transfers = models.IntegerField(validators=max_min(0, 1000))
    points_total = models.IntegerField(validators=max_min(0, 3000))
    team_name = models.CharField(max_length=150)
    team_value = models.IntegerField(validators=max_min(500, 3000))
    transfers_total = models.IntegerField(validators=max_min(0, 570))
