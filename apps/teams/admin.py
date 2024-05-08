from django.contrib import admin
from .models import Team, Participant, TimeCount, TeamParticipant, RoundRobin

admin.site.register(Team)
admin.site.register(Participant)
admin.site.register(TimeCount)
admin.site.register(TeamParticipant)
admin.site.register(RoundRobin)