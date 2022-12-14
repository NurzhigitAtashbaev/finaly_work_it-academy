from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import CertificateSerializer
from .models import OrderCertificate
from .tasks import send_feedback_email_task


class OrderCreateView(generics.ListCreateAPIView):
    """Покупка сертификата"""
    queryset = OrderCertificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminUser]

    def send_email(self):
        send_feedback_email_task.apply_async(args=[
            self.cleaned_data["email"], self.cleaned_data["message"]
        ]
        )
