from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters_
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     CreateAPIView, DestroyAPIView,
                                     ListCreateAPIView)

from .permissions import IsPostOrCommentOwner
from .serializers import (EntrySerializer, CommentSerializer, DeleteCommentSerializer,
                          TourSerializer, CategorySerializer, TypesSerializer,
                          TourCrudSerializer, LikeSerializer)

from .models import Tour, Category, Types, Entry, Comment, Like


class TourDateFilter(filters_.FilterSet):
    """Фильтр для поиска туров по дате и названию """
    start_day = filters_.DateFromToRangeFilter(field_name="start_day")

    class Meta:
        model = Tour
        fields = ['start_day']


class TourListView(ListAPIView):
    """Для просмотра всех туров """
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TourDateFilter
    search_fields = ['title']
    filterset_fields = ['start_day']


class TourDetailView(RetrieveAPIView):
    """Для детального просмотра туров """
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [AllowAny]


#
class CategoryDetailView(RetrieveAPIView):
    """Детальный просмотр по категориям """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class TypesDetailView(RetrieveAPIView):
    """ Для просмотра туров по типам(однодневный, x`двухдневный)"""
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]


class CreateTourViews(CreateAPIView):
    """Создание Туров"""
    queryset = Tour.objects.all()
    serializer_class = TourCrudSerializer
    permission_classes = [IsAdminUser]


class EntryTourViews(CreateTourViews):
    """Запись на тур"""
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (IsAuthenticated,)


class CreateCommentView(ListCreateAPIView):
    """Комментарий к туру"""
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def put(self, request, pk=None):
        user = request.user
        data = request.data
        data['user'] = user.email
        data['tour'] = pk
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid(True):
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response("comment created!", status=status.HTTP_202_ACCEPTED)


class DeleteCommentView(DestroyAPIView):
    """Удаление комментов"""
    queryset = Comment.objects.all()
    serializer_class = DeleteCommentSerializer
    permission_classes = (IsPostOrCommentOwner, IsAuthenticatedOrReadOnly)


class LikeCreateView(ListCreateAPIView):
    """Добавление лайков"""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = IsAuthenticatedOrReadOnly


class LikeDeleteView(DestroyAPIView):
    """Удаление лайков """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsPostOrCommentOwner, IsAuthenticatedOrReadOnly)