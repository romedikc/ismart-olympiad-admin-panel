from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers

from .models import Participant, Team, TeamParticipant, TimeCount, RoundRobin


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'phone_number']


class TeamSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id',
                  'name',
                  'school',
                  'subcategory',
                  'participants',
                  'is_arrived',
                  'is_active',
                  'round_robin_total']
        read_only_fields = ['round_robin_total']


class TeamParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamParticipant
        fields = ['id', 'team', 'participant']


class TimeCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeCount
        fields = ['id',
                  'team',
                  'game',
                  'first_time',
                  'second_time',
                  'third_time',
                  'least_time'
                  ]


class RoundRobinSerializer(serializers.ModelSerializer):
    team1 = PresentablePrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        presentation_serializer=TeamSerializer
    )
    team2 = PresentablePrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        presentation_serializer=TeamSerializer
    )

    class Meta:
        model = RoundRobin
        fields = ['id',
                  'team1',
                  'team2',
                  'score_team1',
                  'score_team2',
                  ]
