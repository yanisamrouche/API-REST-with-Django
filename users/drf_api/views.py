from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListApiView(APIView):
    #1.get all users
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #2.create users
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'gender': request.data.get('gender'),
            'email': request.data.get('email'),

        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
