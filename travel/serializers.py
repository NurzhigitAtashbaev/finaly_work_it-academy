from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Tour, Category, Types, Comment, Entry, Like
from users.serializers import UsersProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    tour = serializers.CharField(source="tour.title")

    class Meta:
        model = Comment
        fields = ('id', 'text', 'image', 'user', 'tour')


class TourSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title")
    types = serializers.CharField(source="types.title")
    comments = CommentSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('id', 'category', 'types', 'title', 'image', 'price', 'start_day', 'end_day', 'comments',
                  'likes_count')

        def get(self, request):
            serializer = TourSerializer(Tour.objects.all(), many=True)


class CategorySerializer(serializers.ModelSerializer):
    tours = serializers.SerializerMethodField()

    def get_tours(self, obj):
        return TourSerializer(obj.tours.all(), many=True).data

    class Meta:
        model = Category
        fields = ('id', 'title', 'tours')


class TypesSerializer(serializers.ModelSerializer):
    tours = serializers.SerializerMethodField()

    def get_tours(self, obj):
        return TourSerializer(obj.tours.all(), many=True).data

    class Meta:
        model = Types
        fields = ('id', 'title', 'tours')


class TourCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


'''Запись на тур,Если мест нету выдаст ошибку'''


class EntrySerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        print(attrs)
        quantity = attrs['tour'].quantity_of_seats
        quantity2 = Entry.objects.filter(tour=attrs['tour']).count()
        if quantity2 >= quantity:
            raise ValidationError(
                {
                    'quantity_of_seats': 'Извините, Все места забронированы! Вы можете записаться на другую дату!'
                }
            )
        return attrs

    class Meta:
        model = Entry
        fields = "__all__"


class DeleteCommentSerializer(serializers.ModelSerializer):
    '''Удаление коментариев Под Турами.
    Коментарий может удалить только тот человек кто его написал'''
    class Meta:
        model = Comment
        fields = ('id', 'user')


class LikeSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if isinstance(instance, Like):
            data['likes_count'] = instance.like
        elif isinstance(instance, Tour):
            likes = Like.objects.filter(tour=instance)
            data['likes_count'] = likes.count()
        return data

    class Meta:
        model = Like
        fields = ('id', 'like', 'user', 'tour', 'likes_count')


class LikeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user')
