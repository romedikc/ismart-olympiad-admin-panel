from accounts.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    date = models.DateField()
    winner = models.CharField(max_length=100)
    judges = models.ManyToManyField(User, related_name='races_judged')

    def __str__(self):
        return self.name

class Participant(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} in {self.race.name}"
