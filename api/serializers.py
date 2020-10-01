from rest_framework import serializers

from boastOrRoast.models import BoastOrRoast


class BoastOrRoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoastOrRoast
        fields = [
            'id',
            'description',
            'is_boast',
            'date',
            'up_votes',
            'down_votes',
            'vote_score',
        ]