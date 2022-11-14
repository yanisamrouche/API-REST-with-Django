from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import GenericAPIView

# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserListApiView(GenericAPIView):

    serializer_class = UserSerializer

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

class UserDetailApiView(GenericAPIView):

    serializer_class = UserSerializer

    def get_userByID(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    #3. get user by id
    def get(self, request, user_id, *args, **kwargs):
        user_instance = self.get_userByID(user_id)
        if not user_instance:
            return Response(
                {"res": "the user id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #4. update user
    def put(self, request, user_id, *args, **kwargs):
        user_instance = self.get_userByID(user_id)
        if not user_instance:
            return Response(
                {"res": "the user id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'gender': request.data.get('gender'),
            'email': request.data.get('email'),
        }
        serializer = UserSerializer(instance=user_instance,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #5. delete user
    def delete(self, request, user_id, *args, **kwargs):
        user_instance = self.get_userByID(user_id)
        if not user_instance:
            return Response(
                {"res": "user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user_instance.delete()
        return Response(
            {"res": "user deleted!"},
            status=status.HTTP_200_OK
        )