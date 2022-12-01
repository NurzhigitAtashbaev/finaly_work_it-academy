from django.urls import path, include
from .views import (
        AttractionsListAPIView,
        AttractionsCreateAPIView,
        AttractionsUpdateAPIView,
        AttractionsRetrieveAPIView,
        AttractionsDestroyAPIView,
    )
urlpatterns = [
    path('', AttractionsListAPIView.as_view()),
    path('create/', AttractionsCreateAPIView.as_view()),
    path('update/', AttractionsUpdateAPIView.as_view()),
    path('detail/<int:pk>/', AttractionsRetrieveAPIView.as_view()),
    path('delete/<int:pk>/', AttractionsDestroyAPIView.as_view()),
]
