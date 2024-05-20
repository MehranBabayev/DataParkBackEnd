from rest_framework import serializers
from apps.users.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,  validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ("name", "email", "surname", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs['password']
        if 'password_confirm' in self.initial_data and password != self.initial_data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        if 'password_confirm' not in self.initial_data:
            raise serializers.ValidationError('it is missed password_confirm')
        return attrs



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
