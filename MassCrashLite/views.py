from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserLocation

@api_view(['POST'])
def save_location(request):
    name = request.data.get('name')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    if name and latitude and longitude:
        location = UserLocation(name=name, latitude=latitude, longitude=longitude)
        location.save()
        return Response({'message': 'Location saved successfully'})
    else:
        return Response({'error': 'Invalid data'})