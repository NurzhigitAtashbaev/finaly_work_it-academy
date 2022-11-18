from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserProfileListCreateView, UserProfileDetailView, UsersViewSet, RegisterUserView

router = DefaultRouter()
router.register('user', UsersViewSet)

urlpatterns = [
    path("profiles/", UserProfileListCreateView.as_view(), name="profiles"),
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include(router.urls)),
    path('reg/', RegisterUserView.as_view()),
]