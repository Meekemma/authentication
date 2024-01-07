from django.urls import path
from . import views
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/password_reset/request/', reset_password_request_token, name='reset_password_request_token'),
    path('api/password_reset/confirm/', reset_password_confirm, name='reset_password_confirm'),

    path('register/', views.registerUsers, name='register'),
    path('change-password/', views.changePasswordView, name='change-password'),
]
