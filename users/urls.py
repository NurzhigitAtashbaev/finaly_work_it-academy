from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    UserProfileListCreateView,
    UserProfileDetailView,
    EmailVerifyAPIView,
    RegisterUserView, PasswordChangeAPIView,
)

urlpatterns = [
    path("profiles/", UserProfileListCreateView.as_view(), name="profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path('change_password/', PasswordChangeAPIView.as_view(), name='change-password'),
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('email/verification/<uuid:email_verify>', EmailVerifyAPIView.as_view(), name='emailActivate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
