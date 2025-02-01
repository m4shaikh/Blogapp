from django.db import models
from django.conf import settings  # Import settings to use AUTH_USER_MODEL

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    blog_pic = models.ImageField(upload_to='blog_pics/', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL
        related_name='liked_blogs',
        blank=True
    )

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use AUTH_USER_MODEL
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
