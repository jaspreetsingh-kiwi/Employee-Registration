from django.contrib.auth.handlers.modwsgi import check_password
from rest_framework import serializers

from .models import EmployeeDetails


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    """
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(max_length=10, required=True)
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True)

    class Meta:
        """
         Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'password2']

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
                raise serializers.ValidationError('Username already taken')
            elif EmployeeDetails.objects.filter(email=email).exists():
                raise serializers.ValidationError('Account with this Email already exists')
        return data

    def create(self, validated_data):
        """
        Override the create method to add custom behavior when creating a new Employee instance
        """
        emp = EmployeeDetails.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        emp.set_password(validated_data['password'])
        emp.save()
        return emp


class LoginSerializer(serializers.ModelSerializer):
    """
     Serializers Login allows user to logged-in.
     """
    username = serializers.CharField(max_length=10, required=True)
    password = serializers.CharField(max_length=10, min_length=8, write_only=True, required=True)

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['username', 'password']

    def validate(self, data):
        """
        Validate if username or password is incorrect.
        """
        username = data.get('username', None)
        password = data.get('password', None)

        emp = EmployeeDetails.objects.filter(username=username).first()
        if emp is not None:
            raise serializers.ValidationError('Username is Incorrect')

        if not check_password(password):
            raise serializers.ValidationError(
                'The provided password is incorrect.'
            )
        return {
            'username': emp.username,
        }


class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
     Serializers EmployeeProfile display the data to logged-in user.
     """
    first_name = serializers.CharField(max_length=20, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(max_length=10, required=True)

    class Meta:
        """
        Use the Meta class to specify the model and fields that the serializer should work with
        """
        model = EmployeeDetails
        fields = ['id', 'first_name', 'last_name', 'email', 'username']
