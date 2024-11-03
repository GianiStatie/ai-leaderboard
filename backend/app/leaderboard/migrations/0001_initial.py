# Generated by Django 5.1.2 on 2024-11-03 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Score",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("best_time", models.FloatField(default=0.0)),
                ("best_level", models.IntegerField(default=0)),
                ("metadata", models.TextField(default="{}")),
            ],
        ),
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ScoreHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.FloatField(default=0.0)),
                ("level", models.IntegerField(default=0)),
                ("metadata", models.TextField(default="{}")),
                (
                    "score_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="leaderboard.score",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="leaderboard.teams",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="score",
            name="team_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="leaderboard.teams"
            ),
        ),
    ]
