from apps.career.api.serializers.city_serializers import  (
     CitySerializer
     
    )

from apps.career.models import  (

    City
    )
from rest_framework.generics import  (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )


class CityListCreateAPIView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer 
    
    
class CityDetealAPIView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer       