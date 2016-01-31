from rest_framework import serializers
from api.models.location import Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'name'
        )