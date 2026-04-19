from django.db import models
from django.core.exceptions import ValidationError

from core_apps.common import choices
from core_apps.common.choices import RegistrationStatus
from core_apps.common.models import AuditModel
# Create your models here.
class Tournament (AuditModel):
    name = models.CharField(max_length=100)
    location =  models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Team(AuditModel):
    name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(AuditModel):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return self.name

class Registration(AuditModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=choices.RegistrationStatus,
        default=RegistrationStatus.PENDING)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team', 'tournament'],
                name='unique_team_tournament'
            )
        ]

    def __str__(self):
        return f"{self.team} - {self.tournament}"