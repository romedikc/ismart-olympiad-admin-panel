from rest_framework import serializers

from .models import Participant, Team, TeamParticipant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'phone_number']


class TeamSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'school', 'subcategory', 'participants']


class TeamParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamParticipant
        fields = ['id', 'team', 'participant']
