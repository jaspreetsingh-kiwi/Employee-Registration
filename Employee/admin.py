from django.contrib import admin
from .models import EmployeeDetails


# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
    """
    Class EmployeeDetailAdmin display all the fields of EmployeeDetails model in admin panel
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'password')


admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
