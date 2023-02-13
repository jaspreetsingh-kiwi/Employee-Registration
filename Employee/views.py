# Create your views here.
from django.contrib import auth
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .messages import CREATED_SUCCESSFULLY, BAD_REQUEST
from .models import EmployeeDetails
from .serializers import RegistrationSerializer, LoginSerializer, EmployeeProfileSerializer


# Create your views here.

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class EmployeeRegisterViewSet(viewsets.ModelViewSet):
    """
    The EmployeeRegisterViewSet class create a new employee for the Employee model.
    """
    queryset = EmployeeDetails
    serializer_class = RegistrationSerializer
    http_method_names = ['post']

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Employee Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def create(self, request, *args, **kwargs):
        """
        Creates a new instance of the Employee model.
        """
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            print(serializer.data)
            return Response({'message': CREATED_SUCCESSFULLY, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': BAD_REQUEST}, status.HTTP_400_BAD_REQUEST)


class EmployeeLoginViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Employee Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            token = get_token_for_user(user)
            return Response({'token': token, 'message': 'Login Successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class EmployeeProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeProfileSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Student Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def list(self, request, *args, **kwargs):
        serializer = EmployeeProfileSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
