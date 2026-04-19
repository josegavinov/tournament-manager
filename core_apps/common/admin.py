from django.contrib import admin
from core_apps.manager.models import Team,Player, Tournament,Registration

# Register your models here.
admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','location', 'start_date', 'end_date')
    search_fields = ('name','location')


admin.site.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','team','tournament')
    search_fields = ('name','team')


admin.site.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name','start_date', 'end_date')
    search_fields = ('name','start_date')

admin.site.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','team','tournament')
    search_fields = ('name','team')


