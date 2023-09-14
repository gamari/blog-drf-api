from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Post, Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")

class PostSerializer(ModelSerializer):
    category = PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        required=False
    )
    author = PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), 
        required=False
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "header_image",
            "category",
            "created_at",
            "updated_at",
            "author",
        )