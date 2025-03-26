# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import *
from .models import *
from .permissions import *

class RegistrationView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'response': "Successfully Registered",
                'username': user.username,
                'email': user.email,
                'role': user.role.name,
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            return Response({
                "message": "Role created successfully",
                "role": RoleSerializer(role).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin] 

    def get(self, request):
        return Response({"message": "This is the Admin Panel"})


class TeacherOnlyView(APIView):
    permission_classes = [IsAuthenticated,IsTeacher] 

    def get(self, request):
        return Response({"message": "This is the Teacher Panel"})

class StudentOnlyView(APIView):
    permission_classes = [IsAuthenticated,IsStudent] 

    def get(self, request):
        return Response({"message": "This is the Student Panel"})
