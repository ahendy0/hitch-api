from models import Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('place_id', 'name', 
        	# 'rides1', 'rides2'
        )


