"""User serializers """

# Django
from django.contrib.auth import authenticate, password_validation

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

# Model
from users.models import User, Profile


class UserModelSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "is_staff",
        ) 

class UserLoginSerializer(serializers.Serializer):
    """User login serializers. 
    Handle the login request data.
    """
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self,data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Email and/or password incorrect.")

        self.context["user"] = user
        return data

    def create(self, data):
        """Regenerate or retrive new token."""
        token, created = Token.objects.get_or_create(user=self.context["user"])

        return self.context["user"], token.key

class UserSignUpSerializer(serializers.Serializer):
    """ User signup serializer. 
    Handles data validation and user/profile creation.
    """
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this email already exists."
            )
        ]
    )
    username = serializers.CharField(
        min_length=2,
        max_length=40,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This username is already taken"
            )
        ]
    )

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # Password 
    password = serializers.CharField(min_length=8, max_length=200)
    password_confirmation = serializers.CharField(min_length=8, max_length=200)

    def validate(self, data):
        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords don't match.")

        password_validation.validate_password(password=password)

        return data

    def create(self, data):
        data.pop("password_confirmation")
        user = User.objects.create_user(**data, is_staff=False)
        Profile.objects.create(user=user)
        return user
