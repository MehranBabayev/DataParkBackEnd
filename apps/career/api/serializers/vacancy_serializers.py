from rest_framework import serializers
from apps.career.models import Vacancy

class VacancyFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ['viewed_ips']
        
        
class VacancyListSerializer(serializers.ModelSerializer):
    city=serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Vacancy
        fields = '__all__'
        
    def get_city(self,obj):

        if obj.city is not None:
            return obj.city.name
        return None
    
    def get_category(self,obj):

        if obj.category is not None:
            return obj.category.name
        return None


class VacancyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'
        
