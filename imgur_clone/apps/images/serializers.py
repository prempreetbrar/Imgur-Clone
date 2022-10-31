from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Image
        read_only_fields = ["id", "owner", "last_modified", "votes"]
        fields =["id", "owner", "title", "image", "description", "last_modified", "votes", "is_public", "tags"]

class UserSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "images"]