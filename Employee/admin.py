from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EmployeeDetails


# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'password')


admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
