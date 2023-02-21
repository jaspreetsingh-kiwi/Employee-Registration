# Create your views here.
import rest_framework_simplejwt.authentication
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .messages import *
from .models import EmployeeDetails
from .serializers import RegistrationSerializer, LoginSerializer, EmployeeProfileSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

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
            return Response({'message': RESPONSE_MESSAGES['registration']['success'], 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginViewSet(viewsets.ModelViewSet):
    """
    The EmployeeLoginViewSet class allows only valid user to log-in.
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
                'message' : RESPONSE_MESSAGES['login']['success'],
            }, status=status.HTTP_200_OK)

        return Response({'errors':serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    """
    The EmployeeProfileViewSet display the data.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeProfileSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of EmployeeDetails Model objects.
        """
        return EmployeeDetails.objects.filter().order_by('id')

    def list(self, request, *args, **kwargs):
        """
         Returns a list of all instances of the EmployeeDetails model.
        """
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves a single instance of the EmployeeDetails model, based on the primary key (pk).
        """
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new instance of the EmployeeDetails model.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            print(serializer.data)
            return Response({'message':SUCCESS_MESSAGES['CREATED_SUCCESSFULLY'] , 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Updates an existing instance of the EmployeeDetails model, based on the primary key (pk).
        """
        emp = self.get_object()
        serializer = self.serializer_class(emp, data=request.data)
        if serializer.is_valid():
            serializer.update(emp, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES["UPDATED_SUCCESSFULLY"], 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Partial Updates an existing instance of the EmployeeDetails model, based on the primary key (pk).
        """
        emp = self.get_object()
        serializer = self.serializer_class(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(emp, serializer.validated_data)
            return Response({'message': SUCCESS_MESSAGES["UPDATED_SUCCESSFULLY"], 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a single instance of the EmployeeDetails model, based on the primary key (pk).
        """
        self.get_object().delete()
        return Response({'message': SUCCESS_MESSAGES["DELETED_SUCCESSFULLY"]})

