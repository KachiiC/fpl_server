import functools
import requests
from fpl_players.models import MatchDay, Player, Chip

ENDPOINT_URL = "https://fantasy.premierleague.com/api"


def fpl_clear():
    # CLEAR ALL FPL DATA STORED
    models = [
        MatchDay,
        Player,
        Chip
    ]

    for model in models:
        model.objects.all().delete()


def fpl_league(league_id):
    LEAGUE_URL = f"{ENDPOINT_URL}/leagues-classic/{league_id}/standings"
    response = requests.get(LEAGUE_URL).json()
    league_players = response['standings']['results']

    for player in league_players:
        fpl_player(player['entry'])


def fpl_player(player_id):
    POINTS_URL = f"{ENDPOINT_URL}/entry/{player_id}/history/"
    points_response = requests.get(POINTS_URL).json()

    PLAYER_SUMMARY = f"{ENDPOINT_URL}/entry/{player_id}/"
    summary_response = requests.get(PLAYER_SUMMARY).json()

    create_fpl_player(summary_response, points_response)


def create_fpl_player(summary, matches):
    transfer_points = []

    for match in matches["current"]:
        transfer_points.append(match["event_transfers_cost"])

        MatchDay(
            bench_points=match["points_on_bench"],
            gameweek=match["event"],
            game_week_points=match["points"],
            player_id=summary["id"],
            points_total=match["total_points"],
            team_value=match["value"],
            transfers=match["event_transfers"],
            transfers_cost=match["event_transfers_cost"],
        ).save()

    for chip in matches["chips"]:
        Chip(
            date=chip["time"],
            name=chip['name'],
            matchday=chip["event"],
            player_id=summary["id"],
        ).save()

    transfer_points_total = functools.reduce(lambda a, b: a + b, transfer_points)

    Player(
        current_gameweek=summary["current_event"],
        last_gameweek_points=summary["summary_event_points"],
        player_id=summary["id"],
        player_name=f"{summary['player_first_name']} {summary['player_last_name']}",
        points_total=summary["summary_overall_points"],
        team_name=summary["name"],
        team_value=summary['last_deadline_value'],
        transfers_total=summary["last_deadline_total_transfers"],
        points_on_transfers=transfer_points_total,
    ).save()


def player_finder(input_id):
    return Player.objects.get(player_id=input_id)


def fpl_sort():
    # ADD MATCHES TO CORRECT PLAYER

    fpl_list = [MatchDay, Chip]

    for item in fpl_list:
        for obj in item.objects.all():
            correct_player = player_finder(obj.player_id)
            if item == MatchDay:
                correct_player.matches.add(obj)
            elif item == Chip:
                correct_player.chips.add(obj)


def fpl_function(input_type, input_id):
    # CLEAR ALL FPL DATA STORED
    fpl_clear()

    # FETCH DEPENDING ON INPUT_TYPE
    if input_type == "player":
        # TAKES INPUT_ID AND CREATES A JSON FILE
        fpl_player(input_id)

    elif input_type == "league":
        # FETCHES A FPL LEAGUE AND CREATES JSON DATA FILE
        fpl_league(input_id)

    fpl_sort()
