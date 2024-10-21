from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/ratings/', views.PostRatingList.as_view(), name='post-rating-list'),
    path('post-ratings/', views.PostRatingCreate.as_view(), name='post-rating-create'),
]
