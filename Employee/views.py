# Create your views here.
from django.contrib import auth
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .messages import CREATED_SUCCESSFULLY, BAD_REQUEST
from .models import EmployeeDetails
from .serializers import RegistrationSerializer, LoginSerializer


# Create your views here.
class EmployeeRegisterViewSet(viewsets.ModelViewSet):
    """
    The EmployeeViewSet class provides the CRUD (Create, Retrieve, Update, Delete) operations for the Employee model.
    """
    queryset = EmployeeDetails

    def get_serializer_class(self):
        """
        The get_serializer_class method returns a ModelSerializer of Employee Model objects.
        """
        if self.action in ['create']:
            return RegistrationSerializer
        return LoginSerializer

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

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return Response({'message': 'Login Successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        auth.logout(request)
        return Response({'message': 'Logout Successful'})
