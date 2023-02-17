# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .messages import *
from .models import EmployeeDetails
from .serializers import RegistrationSerializer, LoginSerializer, EmployeeProfileSerializer
from django.contrib.auth.hashers import check_password


# Create your views here.
class EmployeeRegisterViewSet(viewsets.ModelViewSet):
    """
    The EmployeeRegisterViewSet class create a new employee for the EmployeeDetails model.
    """
    queryset = EmployeeDetails
    serializer_class = RegistrationSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
        Creates a new instance of the Employee model.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES["CREATED_SUCCESSFULLY"], 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginViewSet(viewsets.ModelViewSet):
    """
    The EmployeeLoginViewSet class allows user to log-in.
    """
    queryset =  EmployeeDetails
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        """
        Allows only valid user to login.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message' : SUCCESS_MESSAGES["LOGIN_SUCCESSFULLY"],
            }, status=status.HTTP_200_OK)

        return Response({'errors':serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

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
