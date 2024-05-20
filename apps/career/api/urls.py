from django.urls import path
from apps.career.api.views import vacancy_views,city_views

urlpatterns = [
    path('vacancy-filter/', vacancy_views.VacancyFilterAPIView.as_view()),
    path('vacancy/', vacancy_views.VacancyListCreateAPIView.as_view()),
    # path('vacancy/', vacancy_views.VacancyCreateAPIView.as_view()),
    path('vacancy/<int:pk>/', vacancy_views.VacancyDetealAPIView.as_view()),
    path('city/', city_views.CityListCreateAPIView.as_view()),
]