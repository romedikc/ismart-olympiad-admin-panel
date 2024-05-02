from rest_framework import viewsets

from apps.teams.models import Participant, Team, TeamParticipant
from apps.teams.serializers import TeamParticipantSerializer, TeamSerializer, ParticipantSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamParticipant.objects.all()
    serializer_class = TeamParticipantSerializer
