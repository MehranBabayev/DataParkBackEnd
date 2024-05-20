from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.shortcuts import get_object_or_404
from django.db.models import Q
from apps.career.api.serializers.vacancy_serializers import  (
     VacancyFilterSerializer,
     VacancyListSerializer,
     VacancyCreateSerializer
     
    )

from apps.career.models import  (
    Vacancy,
    VacancyCategory,
    VacancyIPs,
    City
    )
from rest_framework.generics import  (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )

class VacancyListCreateAPIView(ListCreateAPIView):
    queryset = Vacancy.objects.select_related("city","category").prefetch_related("viewed_ips")
    serializer_class = VacancyListSerializer
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return VacancyCreateSerializer
        return super().get_serializer_class()




class VacancyDetealAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializer    


class VacancyFilterAPIView(ListAPIView):
    serializer_class = VacancyFilterSerializer
    queryset = Vacancy.objects.all()
    salary_value = None
    def get_queryset(self):
        filter_object = {}
        for key, value in self.request.query_params.items():
            if key == 'category':
                category = VacancyCategory.objects.filter(name = value).first()
                filter_object[key] = category

            elif key == 'city':
                city = City.objects.filter(name=value).first()
                filter_object[key] = city
                
            elif key == 'min_salary':
                filter_object['min_salary__lte'] = value
                filter_object['max_salary__gte'] = value
                
            else:
                filter_object[key] = value

        queryset = Vacancy.objects.filter(**filter_object)

        return queryset
        
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('level', in_=openapi.IN_QUERY, description='Intern level', type=openapi.TYPE_STRING),
            openapi.Parameter('job_type', in_=openapi.IN_QUERY, description='Job type', type=openapi.TYPE_STRING),
            openapi.Parameter('category', in_=openapi.IN_QUERY, description='Category', type=openapi.TYPE_STRING),
            openapi.Parameter('education', in_=openapi.IN_QUERY, description='Education', type=openapi.TYPE_STRING),
            openapi.Parameter('city', in_=openapi.IN_QUERY, description='City', type=openapi.TYPE_STRING),
            openapi.Parameter('min_salary', in_=openapi.IN_QUERY, description='Salary', type=openapi.TYPE_STRING),
        ])
    def get(self, request):
        try:
            queryset = self.get_queryset()
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("data is wrong", status=status.HTTP_400_BAD_REQUEST)