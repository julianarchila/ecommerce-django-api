""" User views. """

# Django REST Framework
from django.views.generic import detail
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status


# Serializers
from users.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
)

class UserViewSet(GenericViewSet):
    """ User view set. """
    # serializer_class = UserModelSerializer
    def get_serializer_class(self):
        if self.action == "signup":
            return UserSignUpSerializer 
        elif self.action == "login":
            return UserLoginSerializer
        
        return UserModelSerializer


    @action(detail=False,methods=["POST"])
    def signup(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            "message": "ok",
            "user": UserModelSerializer(instance=user).data
        }

        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            "user": UserModelSerializer(user).data,
            "token": token
        }
        return Response(data=data, status=status.HTTP_200_OK)




        
        
        
    