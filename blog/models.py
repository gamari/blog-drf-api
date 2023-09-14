import uuid

from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    header_image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # ここを追加
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title