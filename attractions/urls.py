from django.urls import path
from .views import (
        AttractionsListAPIView,
        AttractionsCreateAPIView,
        AttractionsUpdateAPIView,
        AttractionsRetrieveAPIView,
        AttractionsDestroyAPIView,
    )
urlpatterns = [
    path('', AttractionsListAPIView.as_view(), name='attractions-list'),
    path('create/', AttractionsCreateAPIView.as_view(), name='attractions-create'),
    path('update/', AttractionsUpdateAPIView.as_view(), name='attractions-update'),
    path('detail/<int:pk>/', AttractionsRetrieveAPIView.as_view(), name='attraction-detail'),
    path('delete/<int:pk>/', AttractionsDestroyAPIView.as_view(), name='attraction-delete'),
]
