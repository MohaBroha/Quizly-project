from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """

    confirmed_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "confirmed_password",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def validate(self, attrs):
        password = attrs.get("password")
        confirmed_password = attrs.get("confirmed_password")

        if password != confirmed_password:
            raise serializers.ValidationError(
                {"confirmed_password": "Passwords do not match."}
            )

        return attrs

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")

        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")

        return value

    def create(self, validated_data):

        validated_data.pop("confirmed_password", None)
        return User.objects.create_user(**validated_data)
