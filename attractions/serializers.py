from rest_framework import serializers

from .models import Attractions


class AttractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = '__all__'


class AttractionsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = ('title', 'description')


class AttractionsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Attractions
        fields = ('id',)
