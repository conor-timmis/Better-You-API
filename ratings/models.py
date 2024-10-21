from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} rated {self.post.title} {self.stars} stars"
