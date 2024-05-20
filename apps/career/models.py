from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    
class VacancyCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class VacancyIPs(models.Model):
    view_ip = models.GenericIPAddressField('IP ünvanı', editable=False)

    class Meta:
        verbose_name = ('Vakansiya IP ünvanı')
        verbose_name_plural = ('Vakansiya IP ünvanları')

    def __str__(self) -> str:
        return self.view_ip


class Vacancy(models.Model):

    class Level(models.TextChoices):
        INTERN = 'Intern'
        JUNIOR = 'Junior'
        MIDDLE = 'Middle'
        SENIOR = 'Senior'
        TEAM_LEAD = 'Team Lead'

    class Jobtype(models.TextChoices):
        FULL_TIME = 'full time'
        PART_TIME = 'part time'
        REMOTE = 'remote'


    class Education(models.TextChoices):
        HIGHER = 'Higher'
        SECONDARY = 'Secondary'
        VOCATIONAL_EDUCATION = 'Vocational education'


    header = models.CharField(max_length=300)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    posoting_date = models.DateField(auto_now_add=True)
    expression_date = models.DateField(auto_now_add=True)
    viewed_ips = models.ManyToManyField(VacancyIPs, related_name="vacancies", verbose_name='Vakansiyalar görüntüləndiyi IP ünvanları', editable=False)
    number_of_view = models.IntegerField()
    job_type = models.CharField(max_length=20, choices=Jobtype.choices, default=Jobtype.FULL_TIME)
    category = models.ForeignKey(VacancyCategory, on_delete=models.SET_NULL, blank=True, null=True)
    level = models.CharField(max_length=30, choices=Level.choices, default=Level.INTERN)
    education = models.CharField(max_length=30,choices=Education.choices, default=Education.HIGHER)
    job_description = models.TextField()
    company_site_link = models.URLField(verbose_name='Kampaniyanın veb site linki')
    email_address = models.EmailField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, blank=True, null=True, related_name="vacancies")
    salary_agreement = models.BooleanField(default=False, blank=True, null=True)

