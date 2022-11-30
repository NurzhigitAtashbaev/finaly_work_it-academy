from rest_framework import status
from rest_framework.response import Response
from .permissions import IsPostOrCommentOwner
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView,
                                     get_object_or_404
                                     )
from .serializers import (TourSerializer, CategorySerializer, TypesSerializer, TourCrudSerializer,
                          EntrySerializer, CommentSerializer, DeleteCommentSerializer)
from .models import Tour, Category, Types, Entry, Comment


# Для просмотра всех туров
class TourListView(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [AllowAny]


# для детального просмотра
class TourDetailView(RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [AllowAny]


# для просмотра тура по категориям сложности
class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# для просмотра туров по типам(однодневный и тд)
class TypesDetailView(RetrieveAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]


class CreateTourViews(CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourCrudSerializer
    # permission_classes = [IsAdminUser]


# запись на тур
class EntryTourViews(CreateTourViews):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


# комментарий к туру
class CreateCommentView(ListCreateAPIView):
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


# удаление комментов
class DeleteCommentView(DestroyAPIView):
    serializer_class = DeleteCommentSerializer
    permission_classes = (IsPostOrCommentOwner, IsAuthenticatedOrReadOnly)
    queryset = Comment.objects.all()
