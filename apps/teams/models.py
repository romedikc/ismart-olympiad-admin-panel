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
    is_arrived = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class TeamParticipant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('team', 'participant')

    def __str__(self):
        return f"{self.participant} - {self.team}"


class TimeCount(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    first_score = models.FloatField(default=0.0)
    second_score = models.FloatField(default=0.0)
    third_score = models.FloatField(default=0.0)
    total_time = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.third_score != 0.0:
            self.total_time = self.first_score + self.second_score + self.third_score
        super().save(*args, **kwargs)
