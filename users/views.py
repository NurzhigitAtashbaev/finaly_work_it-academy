from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters_
from rest_framework import viewsets, generics, status
from rest_framework.utils import json
from rest_framework_simplejwt.views import token_obtain_pair

from .models import CustomUser, UserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import (UsersProfileSerializer,
                          UserRegisterSerializer,
                          VerifySerializer,
                          PasswordChangeSerializer,
                          )


class RegisterUserView(generics.CreateAPIView):
    """Регистрация пользователя """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


def check_password(password, password1):
    pass


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    data = {}
    reqBody = json.loads(request.body)
    email1 = reqBody['Email_Address']
    print(email1)
    password = reqBody['password']
    try:

        Account = CustomUser.objects.get()
    except BaseException as e:
        raise ValidationError({"400": f'{str(e)}'})

    token = token_obtain_pair.objects.get_or_create(user=Account)[0].key
    print(token)
    if not check_password(password, Account.password):
        raise ValidationError({"message": "Incorrect Login credentials"})

    if Account:
        if Account.is_active:
            print(request.user)
            login(request, Account)
            data["message"] = "user logged in"
            data["email_address"] = Account.email

            Res = {"data": data, "token": token}

            return Response(Res)

        else:
            raise ValidationError({"400": f'Account not active'})

    else:
        raise ValidationError({"400": f'Account doesnt exist'})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('Пользователь успешно вышел из системы')


class UserProfileListCreateView(generics.ListAPIView):
    """Список Профилей пользователев, Доступно только для Админа"""
    queryset = CustomUser.objects.all()
    serializer_class = UsersProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileFilter(filters_.FilterSet):
    """Фильтр для поиска профиля по username """
    username = filters_.DateFromToRangeFilter(field_name="user")

    class Meta:
        model = UserProfile
        fields = ['user']


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    """Детальный просмотр определённого Профиля, Пока только для Админа"""
    queryset = CustomUser.objects.all()
    serializer_class = UsersProfileSerializer
    filterset_class = UserProfileFilter
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated, IsAdminUser]


class EmailVerifyAPIView(generics.RetrieveAPIView):
    """Верификация gmail пользователя"""
    serializer_class = VerifySerializer
    queryset = CustomUser.objects.filter(is_active=False)

    lookup_field = 'email_verify'

    def retrieve(self, request, *args, **kwargs):
        instance: CustomUser = self.get_object()
        serializer = self.get_serializer(instance)
        instance.email_verificate()
        return Response(serializer.data)


class PasswordChangeAPIView(generics.UpdateAPIView):
    """Смена пароля по email пользователя"""
    serializer_class = PasswordChangeSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
