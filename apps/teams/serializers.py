from rest_framework import serializers

from .models import Participant, Team, TeamParticipant


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'phone_number']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'school', 'subcategory']


class TeamParticipantSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer()

    class Meta:
        model = TeamParticipant
        fields = ['id', 'team', 'participant']
