from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class EmployeeDetails(AbstractUser):
    """
    The Employee model with different fields.
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Employee'

class Department(models.Model):
    """
    The Department model with different fields.
    """
    dept_name = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    dept_size = models.IntegerField()

    class Meta:
        db_table = 'Department'
