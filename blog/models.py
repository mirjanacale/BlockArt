from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = CloudinaryField(
        "image",
        default="https://res.cloudinary.com/dyemjyefz/image/upload/v1746738213/me3fmm8fozl2y69fd4xd.jpg",
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    likes = models.ManyToManyField(User, related_name="blog_posts", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="blog_comments",  
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name="blog_user_comments",  
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

