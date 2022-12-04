from rest_framework import serializers
from .models import Certificate
from travel.serializers import TourSerializer


class CertificateSerializer(serializers.ModelSerializer):
    tour = serializers.SerializerMethodField()

    def get_tour(self, obj):
        all_ = TourSerializer(obj.tours).data
        price = all_.get('price')
        title = all_.get('title')
        return title, price

    class Meta:
        model = Certificate
        fields = ('body', 'count_people', 'sender', 'addressee', 'tours', 'tour',)
