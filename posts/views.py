from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from betteryou_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from .models import Post, PostRating
from .serializers import PostSerializer, PostRatingSerializer

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]
    filterset_fields = [
        'owner__profile',
        'tags',
        'likes__owner__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'title',
        'tags',
        'owner__username',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

class PostRatingCreate(generics.CreateAPIView):
    """
    Create a rating for a post.
    """
    serializer_class = PostRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostRatingList(generics.ListAPIView):
    """
    List ratings for a post.
    """
    serializer_class = PostRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return PostRating.objects.filter(post_id=post_id)
