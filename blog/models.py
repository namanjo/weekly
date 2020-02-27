from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    cover_pic = models.ImageField(blank=True, upload_to='covers')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
