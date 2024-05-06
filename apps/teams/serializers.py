from rest_framework import serializers

from .models import Participant, Team, TeamParticipant, TimeCount


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
                  'is_active']


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
                  'first_score',
                  'second_score',
                  'third_score',
                  'total_time'
                  ]
