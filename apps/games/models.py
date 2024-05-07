from django.db import models

from apps.accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
