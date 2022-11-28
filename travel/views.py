from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,
                                     )
from .serializers import TourSerializer, CategorySerializer, TypesSerializer, TourCrudSerializer, EntrySerializer
from .models import Tour, Category, Types, Entry


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


#запись на тур
class EntryTourViews(CreateTourViews):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

