from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.utils import set_auth_cookies


class RegisterView(CreateAPIView):
    """
    View for registering a new user.
    """

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"detail": "User created successfully!"},
            status=status.HTTP_201_CREATED,
        )


class LoginView(GenericAPIView):
    """
    View for user login.
    """

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.authenticate_user(serializer.validated_data)
        response = self.create_login_response(user)

        return response

    def authenticate_user(self, validated_data):
        user = authenticate(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        if not user:
            raise AuthenticationFailed("Invalid username or password.")

        return user

    def create_login_response(self, user):
        refresh = RefreshToken.for_user(user)

        response = Response(
            {
                "detail": "Login successfully!",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )

        set_auth_cookies(response, str(refresh.access_token), str(refresh))

        return response
