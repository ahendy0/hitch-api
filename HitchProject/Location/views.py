
from models import Location
from rest_framework import viewsets
from serializer import LocationSerializer

# Create your views here.



class LocationViewSet(viewsets.ModelViewSet):

	queryset = Location.objects.all()
	serializer_class = LocationSerializer
