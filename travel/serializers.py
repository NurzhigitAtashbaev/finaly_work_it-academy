from rest_framework import serializers

from users.serializers import UsersProfileSerializer

from rest_framework.exceptions import ValidationError
from .models import Tour, Category, Types, Comment, Entry


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    tour = serializers.CharField(source="tour.title")

    class Meta:
        model = Comment
        fields = ('id', 'text', 'image', 'user', 'tour')

        # def get(self, request):
        #     serializer = TourSerializer(Comment.objects.all(), many=True)
        #     serializer.save()


class TourSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.title")
    types = serializers.CharField(source="types.title")
    comments = CommentSerializer(many=True)

    class Meta:
        model = Tour
        fields = "__all__"

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


class EntrySerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        print(attrs)
        q = attrs['tour'].quantity_of_seats
        q2 = Entry.objects.filter(tour=attrs['tour']).count()
        if q2 >= q:
            raise ValidationError(
                {
                    'tour': 'asdasdasd'
                }
            )
        return attrs

    class Meta:
        model = Entry
        fields = "__all__"


class DeleteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user')




class AdminTourDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        a = UsersProfileSerializer(obj.user).data
        c = a.get('username')
        b = a.get('phone')
        return c, b

    class Meta:
        model = Entry
        fields = ('id', 'tour', 'user')
