from django.db import models

from apps.games.models import Subcategory


class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Team(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, through='TeamParticipant')


class TeamParticipant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('team', 'participant')

    def __str__(self):
        return f"{self.participant} - {self.team}"
