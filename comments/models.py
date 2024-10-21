from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        """Override save method to update the average rating on the related post."""
        super().save(*args, **kwargs)
        self.update_post_average_rating()

    def update_post_average_rating(self):
        """Calculate and update the average rating for the related post."""
        post = self.post
        ratings = post.comments.values_list('rating', flat=True).exclude(rating__isnull=True)
        if ratings:
            post.average_rating = sum(ratings) / len(ratings)
        else:
            post.average_rating = 0
        post.save()
