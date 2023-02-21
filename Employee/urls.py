from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Employee import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Employee-API",
      default_version='v1',
      description="Employee-Details",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
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
   path('employee/', schema_view.with_ui('swagger', cache_timeout=0), name='employee'),

]
