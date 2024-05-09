from django.db import models, transaction

from apps.games.models import Subcategory


class Participant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Team(models.Model):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    GROUP_CHOICES = (
        (FIRST, "First Group"),
        (SECOND, "Second group"),
        (THIRD, "Third group")
    )
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, through='TeamParticipant')
    is_arrived = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_last_sumo_game = models.BooleanField(default=False)
    sumo_group = models.PositiveSmallIntegerField(choices=GROUP_CHOICES,
                                                  null=True, blank=True)
    sumo_total_score = models.PositiveIntegerField(default=0)
    round_robin_total = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return f"{self.school} - {self.name}: {self.subcategory}"


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

    class Meta:
        unique_together = ('team', 'game')

    def save(self, *args, **kwargs):
        if self.third_time != 0.0:
            self.least_time = min(self.first_time, self.second_time, self.third_time)
        super().save(*args, **kwargs)


class RoundRobin(models.Model):
    team1 = models.ForeignKey(Team,
                              related_name="team1_match",
                              on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,
                              related_name="team2_match",
                              on_delete=models.CASCADE)
    score_team1 = models.PositiveIntegerField(default=0)
    score_team2 = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self._previous_score_team1 = 0
            self._previous_score_team2 = 0
        else:
            round_robin_instance = RoundRobin.objects.get(pk=self.pk)
            self._previous_score_team1 = round_robin_instance.score_team1
            self._previous_score_team2 = round_robin_instance.score_team2

        with transaction.atomic():
            team1 = self.team1
            team2 = self.team2

            team1.round_robin_total -= self._previous_score_team1
            team2.round_robin_total -= self._previous_score_team2

            team1.round_robin_total += self.score_team1
            team2.round_robin_total += self.score_team2

            if team1.is_last_sumo_game:
                team1.sumo_total = self.score_team1
            if team2.is_last_sumo_game:
                team2.sumo_total = self.score_team2

            team1.save(update_fields=['round_robin_total', 'sumo_total'])
            team2.save(update_fields=['round_robin_total', 'sumo_total'])

            super().save(*args, **kwargs)
