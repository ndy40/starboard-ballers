from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PlayerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=False, is_superuser=False)


class Player(User):
    class Meta:
        proxy = True

    players = PlayerManager()


class Session(models.Model):
    session_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, related_name='+', on_delete=models.CASCADE, db_index=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    cost = models.DecimalField(decimal_places=2, default=0.00, null=True, max_digits=5)
    max_players = models.IntegerField(default=0, null=True, help_text='Value of 0 allows an infinite number of players')
    players = models.ManyToManyField(Player)

    class Meta:
        ordering = ('session_date',)

    @admin.display
    def number_of_players(self):
        return self.players.all().count()

    def __str__(self):
        return f'{self.venue.name} - {self.session_date}'
