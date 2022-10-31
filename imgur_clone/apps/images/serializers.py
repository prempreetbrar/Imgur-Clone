from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Image
        read_only_fields = ["id", "owner", "last_modified", "votes"]
        fields =["id", "owner", "title", "image", "description", "last_modified", "votes", "is_public", "tags"]