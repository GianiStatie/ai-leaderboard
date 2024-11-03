from rest_framework import serializers

from .models import Teams, Score, ScoreHistory


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teams
        fields = ['name']

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ['team_id', 'best_time', 'best_level', 'metadata']

class ScoreHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScoreHistory
        fields = ['team_id', 'score_id', 'time', 'level', 'metadata']