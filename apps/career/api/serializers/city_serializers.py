from rest_framework import serializers
from apps.career.models import City




class CitySerializer(serializers.ModelSerializer):
   class Meta:
        model = City
        fields = '__all__'
