from datetime import datetime, date

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError

from core_apps.common import choices
from core_apps.common.choices import RegistrationStatus
from core_apps.common.models import AuditModel
# Create your models here.
class Tournament (AuditModel):
    name = models.CharField(max_length=100)
    location =  models.CharField(max_length=100)
    inscription_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name



class Player(AuditModel):
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day)<(self.birth_date.month, self.birth_date.day))
        return age



    def __str__(self):
        return self.name
class Team(AuditModel):
    name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    captain_name = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Category(AuditModel):
    category = models.CharField(max_length=10,choices=choices.Category)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    def __str__(self):
        return self.category


class TournamentCategory(AuditModel):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tournament', 'category'],
                name = 'unique_tournament_category'
            )
        ]
    def __str__(self):
        return f"{self.tournament} - {self.category}"



class Registration(AuditModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament_category = models.ForeignKey(TournamentCategory, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=choices.RegistrationStatus,
        default=RegistrationStatus.PENDING)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'tournament_category'],
                name='unique_team_tournament_category'
            )
        ]

    def __str__(self):
        return f"{self.team} - {self.tournament_category}"

class RosterPlayer(AuditModel):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE,related_name='players')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['player', 'tournament_category'],
                name='unique_player_per_tournament_category'
            ),
            models.UniqueConstraint(
                fields=['registration', 'player'],
                name='unique_player_per_registration'
            )
        ]

    def clean(self):
        tournament_category = self.registration.tournament_category
        category = tournament_category.category
        if not(category.min_age <= self.player.age <= category.max_age):
            raise ValidationError(
                f"El jugador no cumple con la edad para la categoria {category}"
            )

    def __str__(self):
        return f"{self.player} - {self.registration}"