from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    This model represents a 'Like' related to a 'User' (owner) and a 'Post'.
    The 'unique_together' constraint ensures a user
    can't like the same post more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
