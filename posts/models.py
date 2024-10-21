from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Post(models.Model):
    """
    Post model related to a User (owner).
    Default image is set for consistent image URL reference.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = ResizedImageField(
        size=[300, 300], quality=75, upload_to='posts/', 
        default='../default_post_f67djn', blank=True
    )
    tags = models.CharField(
        max_length=100,
        choices=[
            ('Mindfulness', 'Mindfulness'),
            ('Motivation', 'Motivation'),
            ('Personal Growth', 'Personal Growth'),
            ('Time Management', 'Time Management'),
            ('Productivity', 'Productivity'),
            ('Goal Setting', 'Goal Setting'),
            ('Career Development', 'Career Development'),
            ('Leadership', 'Leadership')
        ],
        default='Personal Growth'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


class PostRating(models.Model):
    """
    PostRating model for user ratings on posts.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['post', 'user']
