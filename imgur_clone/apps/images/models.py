from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    title = models.CharField(max_length=20)


class Image(models.Model):
    owner = models.ForeignKey(User, related_name="image", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField(blank=True)
    
    last_modified = models.DateField(auto_now=True)
    votes = models.IntegerField(default=0)
    is_public = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="image", blank=True)

    class Meta:
        ordering = ["-votes"]
