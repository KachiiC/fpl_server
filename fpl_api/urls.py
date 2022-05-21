from django.contrib import admin
from django.urls import path
from fpl_players.views import FplLeagueView, FplPlayerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('league=<str:input_id>', FplLeagueView.as_view(), name="fpl_view"),
    path('player=<str:input_id>', FplPlayerView.as_view(), name="fpl_view"),
]
