from rest_framework import serializers

from .models import CustomUser


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'password2', 'phone')

    def save(self, *args, **kwargs):
        # Создаём объект класса CustomUser
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user


class UserVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('is_active',)
