from django.db import models, transaction

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
    round_robin_total = models.IntegerField(default=0)


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
    first_time = models.FloatField(default=0.0)
    second_time = models.FloatField(default=0.0)
    third_time = models.FloatField(default=0.0)
    least_time = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.third_time != 0.0:
            self.least_time = min(self.first_time, self.second_time, self.third_time)
        super().save(*args, **kwargs)


class RoundRobin(models.Model):
    team1 = models.ForeignKey(Team, related_name="team1_match", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="team2_match", on_delete=models.CASCADE)
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            team1 = self.team1
            team2 = self.team2

            team1.round_robin_total += self.score_team1
            team2.round_robin_total += self.score_team2

            team1.save(update_fields=['round_robin_total'])
            team2.save(update_fields=['round_robin_total'])

            super().save(*args, **kwargs)
