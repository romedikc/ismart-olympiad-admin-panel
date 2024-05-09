from rest_framework import viewsets

from apps.teams.models import Participant, Team, TeamParticipant, TimeCount, RoundRobin
from apps.teams.serializers import TeamParticipantSerializer, TeamSerializer, ParticipantSerializer, \
    TimeCountSerializer, RoundRobinSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ["subcategory"]


class TeamMembershipViewSet(viewsets.ModelViewSet):
    queryset = TeamParticipant.objects.all()
    serializer_class = TeamParticipantSerializer


class TimeCountViewSet(viewsets.ModelViewSet):
    queryset = TimeCount.objects.all()
    serializer_class = TimeCountSerializer
    filterset_fields = ["team__is_arrived", "team__subcategory"]


class RoundRobinViewSet(viewsets.ModelViewSet):
    queryset = RoundRobin.objects.all()
    serializer_class = RoundRobinSerializer
