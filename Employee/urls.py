from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Employee import views

# Creating Router Object
router = DefaultRouter()

"""
Routing for Registration, Login & Display
"""

router.register('register', views.EmployeeRegisterViewSet, basename='register')
router.register('login', views.EmployeeLoginViewSet, basename='login'),
router.register('display', views.EmployeeProfileViewSet, basename='display')

urlpatterns = [
    path('', include(router.urls)),
]
