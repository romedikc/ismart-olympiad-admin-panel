from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.teams.models import Participant, Team, TeamParticipant, TimeCount, RoundRobin
from apps.teams.serializers import TeamParticipantSerializer, TeamSerializer, ParticipantSerializer, \
    TimeCountSerializer, RoundRobinSerializer
from apps.teams.utils import top_teams


class TopTeamsView(APIView):
    def get(self, request):
        group_number = request.query_params.get('group_number')
        group_number = int(group_number)
        if group_number in [Team.FIRST, Team.SECOND, Team.THIRD]:
            teams = top_teams(group_number)
            serializer = TeamSerializer(teams, many=True)
            return Response(serializer.data)

        return Response({"error": "Invalid group number."},
                        status=status.HTTP_400_BAD_REQUEST)


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
