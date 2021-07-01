from user.permissions import IsAdminUserOrOwnAccount
from user.models import UserAccount
from rest_framework.response import Response
from .serializers import (
    LoginSerializer,
    UserAccountSerializer,
)
from django.contrib.auth import authenticate, login as django_login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authtoken.models import Token
from common.views import LoggerAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class LoginView(LoggerAPIView):
    """Class based view loggin in user and returning Auth Token."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        serializer_obj = LoginSerializer(data=data)

        if serializer_obj.is_valid():
            username = serializer_obj.data['username']
            password = serializer_obj.data['password']

            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'}, status=401)

            django_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)

            response_data = UserAccountSerializer(user).data
            response_data["key"] = token.key

            return Response(response_data, status=200)

        return Response(serializer_obj.errors, status=400)


class UserInfo(LoggerAPIView):
    """Check the userinfo of a user"""

    def get(self, request):
        user = request.user
        serializer = UserAccountSerializer(user)
        return Response(serializer.data)


class UserListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.order_by('-id').all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrOwnAccount]
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.order_by('-id').all()
