# DJANGO REST FRAMEWORK
from rest_framework import serializers
# MODELS
from .models import Chip, MatchDay, Player


class ChipSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField("%d/%m/%Y")

    class Meta:
        model = Chip
        fields = [
            "name",
            "matchday",
            "date"
        ]


class MatchDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDay
        fields = [
            'gameweek',
            'game_week_points',
            'points_total',
            'transfers',
            'team_value',
            'transfers_cost',
            'bench_points',
        ]


class PlayerSerializer(serializers.ModelSerializer):
    matches = MatchDaySerializer(many=True, read_only=True)
    chips = ChipSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = [
            'player_id',
            'player_name',
            'team_name',
            'current_gameweek',
            'last_gameweek_points',
            'points_total',
            'transfers_total',
            'points_on_transfers',
            'team_value',
            'chips',
            'matches',
        ]
