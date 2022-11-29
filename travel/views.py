from rest_framework.response import Response
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
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DeleteCommentView(DestroyAPIView):
    serializer_class = DeleteCommentSerializer
    queryset = Comment.objects.get(id=1)
    print(queryset)

    def delete(self, request, *args, **kwargs):
        tour = get_object_or_404(Tour, id=id)
        creator = tour.user.username

        if request.method == "DELETE" and request.user.is_authenticated and request.user.username == creator:
            tour.delete()
            return f"Комментарий удалён "






