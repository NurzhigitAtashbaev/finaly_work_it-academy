from rest_framework import serializers
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
    class Meta:
        model = Entry
        fields = "__all__"


class DeleteCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user')


class TourDateFindSerializers(serializers.ModelSerializer):
    start_day_find = serializers.DateField(write_only=True)
    end_day_find = serializers.DateField(write_only=True)

    class Meta:
        model = Tour
        fields = (
            'id',
            'title',
            'start_day',
            'end_day',
            'start_day_find',
            'end_day_find',
        )

