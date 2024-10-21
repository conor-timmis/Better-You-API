from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from betteryou_api.permissions import IsOwnerOrReadOnly
from django.db.models import Avg

class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        post_id = request.query_params.get('post')
        if post_id:
            queryset = queryset.filter(post_id=post_id)

        average_rating = queryset.aggregate(Avg('rating'))['rating__avg'] or 0

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'comments': serializer.data,
            'average_rating': average_rating,
        })

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by ID if the user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
