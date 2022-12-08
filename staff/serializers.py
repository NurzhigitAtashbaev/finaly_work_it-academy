from rest_framework import serializers

from .models import AboutStaff, Contacts


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStaff
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
