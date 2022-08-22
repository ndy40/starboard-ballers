import decimal

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

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


class Session(models.Model):
    session_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, related_name='+', on_delete=models.CASCADE, db_index=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    cost = models.DecimalField(decimal_places=2, default=0.00, null=True, max_digits=5)
    max_players = models.IntegerField(default=0, null=True, help_text='Value of 0 allows an infinite number of players')
    players = models.ManyToManyField(Player, null=True, blank=True)

    class Meta:
        ordering = ('session_date',)

    @admin.display
    @property
    def number_of_players(self):
        return self.players.all().count()

    @property
    def month_name(self):
        return self.session_date.strftime('%B')

    @property
    def cost_per_player(self):
        try:
            return round((self.cost / self.number_of_players), 2)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f'{self.venue.name} - {self.session_date}'
