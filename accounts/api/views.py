from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.exceptions import TokenError
from accounts.utils import (
    clear_auth_cookies,
    set_access_cookie,
    set_auth_cookies,
)


class RegisterView(CreateAPIView):
    """
    View for registering a new user.
    """

    authentication_classes = []
    permission_classes = [AllowAny]

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

    authentication_classes = []
    permission_classes = [AllowAny]
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


class LogoutView(GenericAPIView):
    """
    View for user logout.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        self.blacklist_token(refresh_token)

        response = Response(
            {
                "detail": "Log-Out successfully! All Tokens will be deleted. Refresh token is now invalid."
            },
            status=status.HTTP_200_OK,
        )

        clear_auth_cookies(response)

        return response

    def blacklist_token(self, refresh_token):
        if not refresh_token:
            return

        token = RefreshToken(refresh_token)
        token.blacklist()


class TokenRefreshView(GenericAPIView):
    """
    View for refreshing the access token.
    """

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        access_token = self.create_access_token(refresh_token)

        response = Response(
            {"detail": "Token refreshed"},
            status=status.HTTP_200_OK,
        )

        set_access_cookie(response, access_token)

        return response

    def create_access_token(self, refresh_token):
        if not refresh_token:
            raise AuthenticationFailed("Refresh token is invalid or missing.")

        try:
            token = RefreshToken(refresh_token)
            return str(token.access_token)
        except TokenError:
            raise AuthenticationFailed("Refresh token is invalid.")
