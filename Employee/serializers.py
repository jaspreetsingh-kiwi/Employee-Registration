from rest_framework import serializers
from .models import EmployeeDetails, Department
from .messages import *
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    """
    first_name = serializers.CharField(max_length=50, min_length=2,trim_whitespace=False,required=True,error_messages=Validation['first_name'])
    last_name = serializers.CharField(max_length=50, required=True, trim_whitespace=False,error_messages=Validation['last_name'])
    email = serializers.EmailField(max_length=30,required=True,trim_whitespace=False,error_messages=Validation['email'])
    username = serializers.CharField(max_length=30, required=True,trim_whitespace=False,error_messages=Validation['username'])
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True,trim_whitespace=False,error_messages=Validation['password'])
    password2 = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True,trim_whitespace=False)

    def validate(self, data):
            """
            Validate if password is correct,username or email already exists.
            """
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            password2 = data.get('password2')

            if EmployeeDetails.objects.filter(username=username).exists():
                raise serializers.ValidationError(Validation['username']['exists'])
            if EmployeeDetails.objects.filter(email=email).exists():
                raise serializers.ValidationError(Validation['email']['exists'])
            if password != password2:
                raise serializers.ValidationError(Validation['password']['do_not_match'])
            return data

    def validate_first_name(self, value):
        """
        Validate first name to ensure it contains only alphabetic characters, and no spaces & should start with capital
        """
        if not value or not value.isalpha() or ' ' in value or not value[0].isupper():
            raise serializers.ValidationError(Validation['first_name']['invalid'])
        return value

    def validate_last_name(self, value):
        """
        Validate last name to ensure it contains only alphabetic characters, and no spaces
        """
        if not value or not value.isalpha() or ' ' in value or not value[0].isupper():
            raise serializers.ValidationError(Validation['last_name']['invalid'])
        return value

    def validate_username(self, value):
        """
        Validate username to ensure it only contains alphanumeric characters and underscores, and no spaces
        """
        if not value or not value.isalnum() or ' ' in value or \
           not any(char.isalpha() for char in value):
           raise serializers.ValidationError(Validation['username']['invalid'])
        return value

    def validate_password(self, value):
        """
        Validate if password contains uppercase, lowercase, digit, space and special character.
        """

        if not value or ' ' in value or \
           not any(char.isupper() for char in value) or \
           not any(char.islower() for char in value) or \
           not any(char.isdigit() for char in value) or \
           not any(char in "!@#$%^&*()-_+=[]{};:'\"<>,.?/\\|" for char in value) or \
           " " in value:
           raise serializers.ValidationError(Validation['password']['invalid'])
        return value

    def create(self, validated_data):
        """
        Override the create method to add custom behavior when creating a new EmployeeDetails instance
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
     Serializers Login allows only valid user to log-in
    """
    username = serializers.CharField(max_length=30, required=True, trim_whitespace=False,
                                     error_messages=Validation['username'])
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True, trim_whitespace=False,
                                     error_messages=Validation['password'])

    def validate(self, data):
        """
        Validate if username and password is incorrect.
        """
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError(RESPONSE_MESSAGES['login']['failed'])

        data['user'] = user
        return data

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['username', 'password']

class DepartmentCreateSerializer(serializers.ModelSerializer):
    """
    Serializers DepartmentCreate creates a new Department.
    """
    dept_name = serializers.CharField(max_length=20, required=True)
    language = serializers.CharField(max_length=20, required=True)
    dept_size = serializers.IntegerField()


    def create(self, validated_data):
        """
        Override the create method to add custom behavior when creating a new Department instance
        """
        dept = Department.objects.create(**validated_data)
        return dept

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = Department
        fields = ['id', 'dept_name', 'language', 'dept_size',]


class DepartmentUpdateSerializer(serializers.ModelSerializer):
    """
    Serializers DepartmentCreate updatess an existing Department.
    """
    dept_name = serializers.CharField(max_length=20, required=True)
    language = serializers.CharField(max_length=20, required=True)
    dept_size = serializers.IntegerField()

    def update(self, instance, validated_data):
        """
         Override the update method to add custom behavior when updating an existing Employee instance
        """
        dept = Department.objects.filter(id=instance.id).update(
            dept_name=validated_data['dept_name'],
            language=validated_data['language'],
            dept_size=validated_data['dept_size'],
        )
        return dept

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = Department
        fields = ['id', 'dept_name', 'language', 'dept_size', ]
