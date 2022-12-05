from django.urls import path
from .views import OrderCertificateView

urlpatterns = [
    path('certificate/', OrderCertificateView.as_view()),
]