from rest_framework import serializers
from .models import OrderCertificate
from travel.serializers import TourSerializer


class CertificateSerializer(serializers.ModelSerializer):
    tour = serializers.SerializerMethodField()

    def get_tour(self, obj):
        all_ = TourSerializer(obj.tours).data
        price = all_.get('price')
        title = all_.get('title')
        return title, price

    class Meta:
        model = OrderCertificate
        fields = ('tours', 'info', 'count_people', 'phone', 'email', 'sender', 'addressee', 'tour')
