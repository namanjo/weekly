from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length = 100, blank=True, null=True)
    cover_pic = models.ImageField(blank=True, upload_to='covers')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

def blog_pre_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_pre_reciver, sender=Blog)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
