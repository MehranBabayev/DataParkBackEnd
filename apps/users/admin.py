from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('name', 'surname', 'email', 'is_active', 'is_staff','is_superuser')
    list_filter = ('is_active', 'is_staff','is_superuser')
    search_fields = ('name', 'surname', 'email')
    ordering = ('name',)
    readonly_fields = ('created_at',)
    list_display_links = ('name',)


    fieldsets = (
        (None, {'fields': ('name', 'surname', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'surname', 'password1', 'password2', 'is_active', 'is_staff','is_superuser'),
        }),
    )

    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)


