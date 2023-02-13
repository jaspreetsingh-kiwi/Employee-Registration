from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Employee import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

# Creating Router Object
router = DefaultRouter()

router.register('employee', views.EmployeeRegisterViewSet, basename='employee')
router.register('login', views.EmployeeLoginViewSet, basename='login'),
router.register('display', views.EmployeeProfileViewSet, basename='display')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
