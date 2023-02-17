from rest_framework import serializers
from .models import EmployeeDetails
from .messages import *
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    """
    first_name = serializers.CharField(max_length=20, required=True,error_messages={'required': ERROR_MESSAGES["FIRST_NAME_REQUIRED"]})
    last_name = serializers.CharField(max_length=20, required=True, error_messages={'required': ERROR_MESSAGES["LAST_NAME_REQUIRED"]})
    email = serializers.EmailField(required=True, error_messages={'required':  ERROR_MESSAGES["EMAIL_REQUIRED"]})
    username = serializers.CharField(max_length=10, required=True, error_messages={'required':ERROR_MESSAGES["USERNAME_REQUIRED"]})
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True,error_messages={'required': ERROR_MESSAGES["PASSWORD_REQUIRED"]})
    password2 = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True,error_messages={'required': ERROR_MESSAGES["PASSWORD_CONFIRMED"]})

    def validate(self, data):
            """
            Validate if password is correct,username or email already exists.
            """
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            password2 = data.get('password2')

            if password == password2:
                if EmployeeDetails.objects.filter(username=username).exists():
                    raise serializers.ValidationError(ERROR_MESSAGES["USERNAME_EXISTS"])
                elif EmployeeDetails.objects.filter(email=email).exists():
                    raise serializers.ValidationError(ERROR_MESSAGES["EMAIL_EXISTS"])
                else :
                    raise serializers.ValidationError(ERROR_MESSAGES[ "PASSWORDS_DO_NOT_MATCH"])
            return data

    def validate_first_name(self, value):
        """
        Validate first name to ensure it contains only alphabetic characters, and no spaces
        """
        if not value.isalpha() or ' ' in value:
            raise serializers.ValidationError(ERROR_MESSAGES["INVALID_FIRST_NAME"])
        return value


    def validate_last_name(self, value):
        """
        Validate last name to ensure it contains only alphabetic characters, and no spaces
        """
        if not value.isalpha() or ' ' in value:
            raise serializers.ValidationError(ERROR_MESSAGES["INVALID_LAST_NAME"])
        return value

    def validate_email(self, value):
        """
        Validate email address to ensure it is in a valid format, and contains no spaces
        """
        if ' ' in value or '@' not in value:
            raise serializers.ValidationError(ERROR_MESSAGES["INVALID_EMAIL"])
        return value

    def validate_username(self, value):
        """
        Validate username to ensure it only contains alphanumeric characters and underscores, and no spaces
        """
        if not value.isalnum() or ' ' in value:
            raise serializers.ValidationError(ERROR_MESSAGES["INVALID_USERNAME"])
        return value

    def validate_password(self, value):
        """
        Validate if password contains uppercase, lowercase, digit, space and special character.
        """
        if not any(char.isupper() for char in value) or \
           not any(char.islower() for char in value) or \
           not any(char.isdigit() for char in value) or \
           not any(char in "!@#$%^&*()-_+=[]{};:'\"<>,.?/\\|" for char in value) or \
           " " in value:
           raise serializers.ValidationError(ERROR_MESSAGES["INVALID_PASSWORD"])
        return value

    def create(self, validated_data):
        """
        Override the create method to add custom behavior when creating a new Employee instance
        """
        password2 = validated_data.pop('password2')
        emp = EmployeeDetails.objects.create(**validated_data)
        emp.set_password(validated_data['password'])
        emp.save()
        return emp

    class Meta:
        """
         Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'password2']

class LoginSerializer(serializers.ModelSerializer):
    """
     Serializers Login allows user to log-in
    """
    username = serializers.CharField(max_length=10, required=True, error_messages={'required': ERROR_MESSAGES["USERNAME_REQUIRED"]})
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True, error_messages={'required': ERROR_MESSAGES["PASSWORD_REQUIRED"]})

    def validate(self, data):
        """
        Validate if username or password is incorrect.
        """
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Incorrect credentials')

        data['user'] = user
        return data

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['username', 'password']

class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
    Serializers EmployeeProfile display the data to logged-in user.
    """
    first_name = serializers.CharField(max_length=20, required=True,error_messages={'required': ERROR_MESSAGES["FIRST_NAME_REQUIRED"]})
    last_name = serializers.CharField(max_length=20, required=True,error_messages={'required': ERROR_MESSAGES["LAST_NAME_REQUIRED"]})
    email = serializers.EmailField(required=True, error_messages={'required': ERROR_MESSAGES["EMAIL_REQUIRED"]})
    username = serializers.CharField(max_length=10, required=True,error_messages={'required': ERROR_MESSAGES["USERNAME_REQUIRED"]})

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['id', 'first_name', 'last_name', 'email', 'username']
