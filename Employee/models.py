# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class EmployeeDetails(AbstractUser):
    """
    The Employee model with different fields.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)

    class Meta:
        db_table = 'Employee'

