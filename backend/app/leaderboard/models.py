from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Score(models.Model):
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    best_time = models.FloatField(default=0.0)
    best_level = models.IntegerField(default=0)
    metadata = models.TextField()

class ScoreHistory(models.Model):
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)
    score_id = models.ForeignKey(Score, on_delete=models.CASCADE)
    time = models.FloatField(default=0.0)
    level = models.IntegerField(default=0)
    metadata = models.TextField()