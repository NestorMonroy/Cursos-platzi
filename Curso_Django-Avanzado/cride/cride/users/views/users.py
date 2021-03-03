"""Users views
    http://www.cdrf.co/
"""

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
    AccountVerificationSerializer
)


class UserLoginAPIView(APIView):
    """User Login API View"""

    def post(self, request, *args, **kwargs):
        """Hande HTTP POST request """
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """ User sing up API view"""

    def post(self, request, *args, **kwargs):
        """Hande HTTP POST request """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        data =  UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)




class AccountVerificationAPIView(APIView):
    """ Account verification API view"""

    def post(self, request, *args, **kwargs):
        """Hande HTTP POST request """
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'Congratulations, now go share some rides!'}
        return Response(data, status=status.HTTP_200_OK)

