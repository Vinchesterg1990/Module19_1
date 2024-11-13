from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=180)
    balance = models.DecimalField(max_digits=10000, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=180)
    cost = models.DecimalField(max_digits=5000, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="game")

    def __str__(self):
        return self.title
