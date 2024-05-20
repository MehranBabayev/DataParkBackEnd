from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import CustomUser
from .serializers import RegistrationSerializer, LoginSerializer,  PasswordResetSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import PasswordResetForm




class RegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(serializer.validated_data['password'])
        instance.save()


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        if email and password:
            user_obj = CustomUser.objects.filter(email__iexact=email).first()

            if user_obj and user_obj.check_password(password):
            
                serializer = LoginSerializer(user_obj)
                data_list = {}
                data_list.update(serializer.data)
                return Response({"message": "Login successful", "data": data_list, "code": 200})
            else:
                message = "Invalid email or password"
                return Response({"message": message, "code": 401, 'data': {}})
        else:
            message = "Invalid login details."
            return Response({"message": message, "code": 400, 'data': {}})


class PasswordResetAPI(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            form = PasswordResetForm(data={'email': email})
            user_obj = CustomUser.objects.filter(email__iexact=email).first()            
            if form.is_valid():                
                if user_obj:                    
                    form.save(request=request)                   
                    return Response({'detail': 'Password reset email has been sent.'})
                else:
                    return Response({'detail': 'No account found with this email address.'})
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



