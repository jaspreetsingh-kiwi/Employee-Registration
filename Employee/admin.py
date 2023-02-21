from django.contrib import admin
from .models import EmployeeDetails, Department


# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
    """
    Class EmployeeDetailAdmin display all the fields of EmployeeDetails model in admin panel
    """
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    """
    Class DepartmentAdmin display all the fields of Department model in admin panel
    """
    list_display = ('id', 'dept_name', 'language', 'dept_size')

admin.site.register(Department, DepartmentAdmin)
