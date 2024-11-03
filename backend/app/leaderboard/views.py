from rest_framework import viewsets

from .models import Teams, Score, ScoreHistory
from .serializers import TeamSerializer, ScoreSerializer, ScoreHistorySerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreHistoryViewSet(viewsets.ModelViewSet):
    queryset = ScoreHistory.objects.all()
    serializer_class = ScoreHistorySerializer