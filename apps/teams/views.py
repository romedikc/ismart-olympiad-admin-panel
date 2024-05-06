from rest_framework import viewsets

from apps.teams.models import Participant, Team, TeamParticipant, TimeCount
from apps.teams.serializers import TeamParticipantSerializer, TeamSerializer, ParticipantSerializer, TimeCountSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamParticipant.objects.all()
    serializer_class = TeamParticipantSerializer


class TimeCountViewSet(viewsets.ModelViewSet):
    queryset = TimeCount.objects.all()
    serializer_class = TimeCountSerializer
