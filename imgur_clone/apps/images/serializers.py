from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        read_only_fields = ["id", "owner", "last_modified", "votes"]
        fields =["id", "title", "image", "description", "last_modified", "votes", "is_public", "tags"]