from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='all_posts')
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.title


