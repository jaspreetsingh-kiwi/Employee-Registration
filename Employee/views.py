# Create your views here.
from django.contrib import auth
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .messages import CREATED_SUCCESSFULLY, BAD_REQUEST
from .models import EmployeeDetails, get_token_for_user
from .serializers import RegistrationSerializer, LoginSerializer, EmployeeProfileSerializer


# Create your views here.

# def get_token_for_user(user):
#     """
#         Used to generate both refresh and access token
#     """
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token)
#     }


class EmployeeRegisterViewSet(viewsets.ModelViewSet):
    """
        The EmployeeRegisterViewSet class create a new employee for the EmployeeDetails model.
    """
    queryset = EmployeeDetails
    serializer_class = RegistrationSerializer
    http_method_names = ['post']

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of EmployeeDetails Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def create(self, request, *args, **kwargs):
        """
        Creates a new instance of the Employee model.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': CREATED_SUCCESSFULLY, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': BAD_REQUEST}, status.HTTP_400_BAD_REQUEST)


class EmployeeLoginViewSet(viewsets.ModelViewSet):
    """
    The EmployeeLoginViewSet class allows user to log-in.
    """
    queryset = EmployeeDetails
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of EmployeeDetails Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def create(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            auth.login(request, user)
            token = get_token_for_user(user)
            return Response({'token': token, 'message': 'Login Successful'})


class EmployeeProfileViewSet(viewsets.ModelViewSet):
    """
        The EmployeeProfileViewSet display the data.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeProfileSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of Student Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def list(self, request, *args, **kwargs):
        """
        Returns a list of all instances of the EmployeeDetails model.
        """
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
