from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

from .views import (
    UserProfileListCreateView,
    UserProfileDetailView,
    UsersViewSet,
    EmailVerifyAPIView,
    RegisterUserView, ChangePasswordView,
)

router = DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path("profiles/", UserProfileListCreateView.as_view(), name="profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('reg/', RegisterUserView.as_view()),
    path('email/verification/<uuid:email_verify>', EmailVerifyAPIView.as_view(), name='emailActivate'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
