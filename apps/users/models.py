from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager



class CustomUser(AbstractUser):
    name = models.CharField('İstifadəçinin adı', max_length=100)
    surname = models.CharField('Istifadəçinin soyadı', max_length=100)
    email = models.EmailField('İstifadəçinin email ünvanı', unique=True)
    password = models.CharField('İstifadəçinin parolu', max_length=100)
    created_at = models.DateTimeField('İstifadəçinin yaradılma tarixi', auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    class Meta:
        verbose_name = ('İstifadəçi')
        verbose_name_plural = ('İstifadəçilər')

    def __str__(self) -> str:
        return self.name


