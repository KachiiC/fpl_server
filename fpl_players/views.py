# DJANGO REST FRAMEWORK
from rest_framework import views
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# DJANGO TOOLS
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# SERIALIZERS
from .models import Player
from .serializers import PlayerSerializer
# TOOLS
from tools.fpl_tools import fpl_function, player_finder


class FplLeagueView(views.APIView):
    @method_decorator(cache_page(60 * 60))
    def get(self, request, input_id):
        # CREATE FPL PLAYER DATA
        fpl_function("league", input_id)
        # SERIALIZE ALL PLAYERS
        serializer = PlayerSerializer(
            Player.objects.all(),
            many=True,
            context={'request': request}
        ).data

        return Response(serializer, status=HTTP_200_OK)


class FplPlayerView(views.APIView):
    @method_decorator(cache_page(60 * 60))
    def get(self, request, input_id):
        # CREATE FPL PLAYER DATA
        fpl_function("player", input_id)
        # SERIALIZER FPL PLAYER DATA
        serializer = PlayerSerializer(
            player_finder(input_id),
            context={'request': request}
        ).data

        return Response(serializer, status=HTTP_200_OK)
