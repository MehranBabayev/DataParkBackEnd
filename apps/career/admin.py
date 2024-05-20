from django.contrib import admin
from apps.career.models import Vacancy, VacancyCategory, VacancyIPs, City
# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['header', 'min_salary', 'max_salary', 'job_type', 'category', 'level', 'education', 'job_description']

@admin.register(VacancyCategory)
class VacancyCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(VacancyIPs)
class VacancyIPsAdmin(admin.ModelAdmin):
    list_display = ['view_ip']


admin.site.register(City)