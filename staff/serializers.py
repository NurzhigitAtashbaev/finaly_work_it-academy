from rest_framework import serializers

<<<<<<< HEAD
=======

>>>>>>> cceb02a (cleaning + staff view, serializers,urls)
from .models import AboutStaff, Contacts


class StaffListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStaff
<<<<<<< HEAD
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
=======
        fields = '__all__'
>>>>>>> cceb02a (cleaning + staff view, serializers,urls)
